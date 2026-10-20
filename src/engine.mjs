/** BoundaryLab: deterministic scenario engine. Illustrative model, NOT fitted to respondents. */
export const CATEGORIES = ['Groceries','Ready meals','Essentials','Personal care'];
export const CONTEXTS = ['Home','Work'];
export const TIERS = {
  basic:    {name:'Baseline', score:45, courierCost:2.20, carbonG:710, label:'Unverified baseline assumptions'},
  verified: {name:'Verified safeguards', score:76, courierCost:3.15, carbonG:735, label:'Documented pay & complaint pathway (illustrative)'},
  enhanced: {name:'Enhanced safeguards',score:94,courierCost:4.40,carbonG:755,label:'Additional leave, safety & weather protection (illustrative)'}
};
export const DEFAULT = Object.freeze({category:'Groceries',context:'Home', fee:2.99,eta:25,reliability:95, tier:'verified',basket:25, merchandiseMargin:0.23, monthlyIntents:11000, capacity:1550, fixedCost:850, minSafeguard:70});
const clip=(x,min,max)=>Math.max(min,Math.min(max,x));
const sigmoid = z => 1/(1+Math.exp(-z));
export function validateConfig(c){
  if(!CATEGORIES.includes(c.category)||!CONTEXTS.includes(c.context)||!TIERS[c.tier])throw Error('Unknown category, context or safeguards tier');
  for(const [k,lo,hi] of [['fee',0,20],['eta',5,180],['reliability',0,100],['basket',1,1000],['merchandiseMargin',0,1],['monthlyIntents',0,1000000],['capacity',0,1000000],['fixedCost',0,10000000],['minSafeguard',0,100]]){
    if(!Number.isFinite(c[k])||c[k]<lo||c[k]>hi)throw Error(`Invalid ${k}`);
  }
  return c;
}
export function evaluate(person,c){
  // Ordered gates: reason is first failed condition, not a causal decomposition.
  if(!person.category_allow[c.category])return {reason:'Category',interest:0,qualified:false};
  if(!person.context_allow.includes(c.context))return {reason:'Context',interest:0,qualified:false};
  if(TIERS[c.tier].score < person.minimum_courier_safeguard)return {reason:'Courier safeguards',interest:0,qualified:false};
  if(c.fee > person.maximum_fee_gbp)return {reason:'Delivery fee',interest:0,qualified:false};
  if(c.eta > person.maximum_eta_minutes)return {reason:'ETA',interest:0,qualified:false};
  if(c.reliability < person.minimum_reliability_pct)return {reason:'Reliability',interest:0,qualified:false};
  // Chosen coefficients are demonstrative design assumptions and NOT estimated by the interview study.
  const raw= -0.68 + 1.7*person.convenience_need -0.38*c.fee*person.value_sensitivity/3
    -0.3*c.eta/45 + 0.5*(c.reliability-90)/10
    +0.14*(TIERS[c.tier].score-65)/30*person.ethical_salience;
  return {reason:'Qualified',interest:clip(sigmoid(raw),0,1),qualified:true};
}
export function unitEconomics(c){
  validateConfig(c);
  const tier=TIERS[c.tier];
  const speedPremium=c.eta<=20?1.1:c.eta<=30?.55:0;
  const operationCost=1.65;
  const variableCost=tier.courierCost + operationCost + speedPremium;
  const merchandiseContribution=c.basket*c.merchandiseMargin;
  return {variableCost,merchandiseContribution,speedPremium,courierCost:tier.courierCost, contributionPerOrder:merchandiseContribution+c.fee-variableCost,
    assumedCarbonG:Math.max(150,tier.carbonG+(c.eta<=20?200:c.eta>=40?-130:0))};
}
export function aggregate(panel,c){
  validateConfig(c);
  if(!Array.isArray(panel)||panel.length===0)throw Error('Panel required');
  const reasons={Category:0,Context:0,'Courier safeguards':0,'Delivery fee':0,ETA:0,Reliability:0,Qualified:0};
  let eligible=0, propensity=0;const segments={};
  for(const person of panel){
    const e=evaluate(person,c);
    reasons[e.reason]++;
    const seg=segments[person.segment]??(segments[person.segment]={n:0,eligible:0,interest:0});
    seg.n++; if(e.qualified){eligible++;seg.eligible++;}
    propensity+=e.interest; seg.interest+=e.interest;
  }
  const theoreticalDemand=c.monthlyIntents*propensity/panel.length;
  const fulfilled=Math.min(theoreticalDemand,c.capacity);
  const conversion=propensity/panel.length;
  const economics=unitEconomics(c);
  const grossContribution=fulfilled*economics.contributionPerOrder;
  return {n:panel.length,eligible,qualifiedRate:eligible/panel.length,acceptanceRate:conversion,reasons,segments,
    demand:theoreticalDemand,fulfilled,unfulfilled:Math.max(0,theoreticalDemand-fulfilled),capacityUtilization:c.capacity?fulfilled/c.capacity:0,
    grossContribution,netContribution:grossContribution-c.fixedCost, monthlyFixed:c.fixedCost,
    modelCarbonKg:fulfilled*economics.assumedCarbonG/1000, ...economics};
}
export function optimise(panel,base,{minSafeguard=70,minRate=.12}={}){
  const all=[];
  for(const tier of Object.keys(TIERS)){
    if(TIERS[tier].score<minSafeguard)continue;
    for(const eta of [15,20,25,30,35,45])for(const fee of [1.49,1.99,2.49,2.99,3.49,3.99,4.49]){
      const config={...base,tier,eta,fee}; const result=aggregate(panel,config);
      all.push({config,rate:result.acceptanceRate,net:result.netContribution,fulfilled:result.fulfilled,carbonKg:result.modelCarbonKg,viable:result.acceptanceRate>=minRate});
    }
  }
  const feasible=all.filter(x=>x.viable);
  const frontier=feasible.filter(a=>!feasible.some(b=>(b.rate>=a.rate && b.net>=a.net)&&(b.rate>a.rate||b.net>a.net))).sort((a,b)=>a.rate-b.rate);
  return {all,frontier,best:feasible.sort((a,b)=>b.net-a.net)[0]??null};
}
export function sampleSizeTwoProportions(p0,lift,alpha=.05,power=.8){
  if(!(p0>0&&p0<1&&lift>0&&p0+lift<1))throw Error('Invalid baseline or effect size');
  if(alpha!==.05||power!==.8)throw Error('Only prespecified alpha=.05, power=.8 supported');
  const p1=p0+lift,pBar=(p0+p1)/2,zAlpha=1.95996398454005,zPower=.8416212335729143;
  const n=((zAlpha*Math.sqrt(2*pBar*(1-pBar))+zPower*Math.sqrt(p0*(1-p0)+p1*(1-p1)))**2)/(lift**2);
  return Math.ceil(n);
}
export function assumptionsAudit(c){return [
  {dimension:'Customer profiles',status:'Synthetic',explanation:'Generated profiles, not participants from Salonee’s research'},
  {dimension:'Offer thresholds',status:'Synthetic',explanation:'Fee, ETA, reliability and safeguard thresholds are illustrative'},
  {dimension:'Courier safeguard score',status:'Proxy',explanation:'Not a legal or independent employment-standard certification'},
  {dimension:'Financial parameters',status:'User-assumed',explanation:`£${c.basket} basket and ${(c.merchandiseMargin*100).toFixed(0)}% margin are illustrative`},
  {dimension:'Research insight',status:'Reported synopsis',explanation:'Qualitative interpretation from user-provided application documents, not full dissertation'},
  {dimension:'Conversion and contribution',status:'Model output',explanation:'Scenario outputs, not validated forecasts or observed business performance'}
];}
