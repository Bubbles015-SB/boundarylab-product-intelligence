#!/usr/bin/env python3
"""Create a compact, explicit-provenance PDF walkthrough for portfolio review."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT.parent/'BoundaryLab_Portfolio_Case_Study.pdf'
W,H=A4
INK=HexColor('#193d3b');TEAL=HexColor('#275f55');MUTED=HexColor('#71877d');PALE=HexColor('#eaf0e6');CORAL=HexColor('#bd7756');LINE=HexColor('#d9e4d9');BG=HexColor('#f8f9f5')
C=canvas.Canvas(str(OUTPUT),pagesize=A4)
C.setTitle('BoundaryLab | Conditional Adoption Portfolio Case Study')
C.setAuthor('Research-inspired portfolio study prepared for Salonee Shrigandhamurthy')
styles={'body':ParagraphStyle('b',fontName='Helvetica',fontSize=10,leading=15,textColor=INK,spaceAfter=0),
        'small':ParagraphStyle('s',fontName='Helvetica',fontSize=8.7,leading=13,textColor=MUTED),
        'label':ParagraphStyle('l',fontName='Helvetica-Bold',fontSize=9,leading=13,textColor=TEAL),
        'fine':ParagraphStyle('f',fontName='Helvetica',fontSize=7,leading=10.5,textColor=MUTED)}

def para(txt,x,y,width,style='body'):
 p=Paragraph(txt,styles[style]); tw,th=p.wrap(width,800);p.drawOn(C,x,y-th);return y-th

def header(n,section):
 C.setFillColor(BG);C.rect(0,0,W,H,fill=1,stroke=0)
 C.setFillColor(INK);C.setFont('Helvetica-Bold',15);C.drawString(42,H-47,'BOUNDARYLAB')
 C.setFillColor(MUTED);C.setFont('Helvetica-Bold',7.6);C.drawRightString(W-42,H-43,section.upper())
 C.setStrokeColor(LINE);C.line(42,H-57,W-42,H-57)
 C.setFont('Helvetica',7);C.setFillColor(MUTED);C.drawString(42,35,'RESEARCH-INSPIRED PRODUCT ANALYTICS  |  SYNTHETIC DATA ONLY')
 C.drawRightString(W-42,35,f'{n} / 3')

def box(x,y,w,h,color=PALE):
 C.setFillColor(color);C.roundRect(x,y-h,w,h,10,fill=1,stroke=0)

def section_title(x,y,t):
 C.setFillColor(INK);C.setFont('Helvetica-Bold',13);C.drawString(x,y,t)

# P1
header(1,'The research insight')
C.setFillColor(TEAL);C.setFont('Helvetica-Bold',9);C.drawString(42,H-87,'CONDITIONAL ADOPTION INTELLIGENCE')
C.setFillColor(INK);C.setFont('Helvetica-Bold',31);C.drawString(42,H-132,'Not will they use it.')
C.setFillColor(TEAL);C.drawString(42,H-169,'Under what conditions?')
para('An interactive research-to-decision laboratory inspired by Salonee\'s MSc Management work on rapid-delivery adoption. Designed to demonstrate product discovery, operational judgement, stakeholder communication and analytical experimentation.',42,H-193,505)
box(42,H-261,510,96)
C.setFillColor(TEAL);C.setFont('Helvetica-Bold',10);C.drawString(59,H-283,'THE REPORTED QUALITATIVE INSIGHT')
para('After eleven interviews, the study was described as shifting from a yes/no adoption framing to an understanding that acceptability depended on individual conditions: product category, home/work context and treatment of delivery couriers.',59,H-293,474,'body')
C.setFillColor(MUTED);C.setFont('Helvetica-Bold',9);C.drawString(42,H-388,'THE PROTOTYPE')
img=Image.open(ROOT/'media'/'overview.png')
# main content crop removes sidebar and footer for legibility
im=img.crop((210,100,1170,670))
ri=ImageReader(im)
C.drawImage(ri,54,128,width=486,height=294,mask='auto',preserveAspectRatio=False)
C.setFillColor(MUTED);C.setFont('Helvetica',8);C.drawString(42,110,'Interactive web interface: research framing, synthetic scenario metrics and evidence limitations.')
C.showPage()
# P2
header(2,'From evidence to implementation')
C.setFillColor(INK);C.setFont('Helvetica-Bold',23);C.drawString(42,H-105,'How the system works')
para('Reported qualitative themes motivate <b>testable product requirements</b>. A deterministic simulator then demonstrates hypothetical trade-offs - without presenting its outcomes as real customer data.',42,H-119,510)
items=[
 ('01  Research traceability','Reported claim → product requirement → hypothesis → metric. Each claim includes a limit on what can be inferred.'),
 ('02  Personal eligibility','Category, context and courier-treatment safeguards act as hard vetoes before any price or speed calculation.'),
 ('03  Scenario economics','Variable costs, fixed overhead, operational capacity and illustrative interest lead to an explicitly fictional contribution scenario.'),
 ('04  Constrained decisions','Up to 126 parameter combinations and a Pareto comparison reveal trade-offs under a declared minimum safeguard standard.'),
 ('05  Experimentation','A/B-test preregistration, approximate sample sizing, primary outcomes and worker-safety guardrails guide next steps.')]
y=H-185
for title,description in items:
 box(42,y,510,72,HexColor('#edf3ec'))
 C.setFillColor(TEAL);C.setFont('Helvetica-Bold',10);C.drawString(57,y-22,title)
 para(description,57,y-31,482,'small')
 y-=86
box(42,171,510,77,HexColor('#fff4ea'))
C.setFillColor(CORAL);C.setFont('Helvetica-Bold',11);C.drawString(57,151,'MODELLING LIMITATION')
para('The 1,200 synthetic profiles and all quantitative thresholds, conversions, price sensitivities and financial outputs are demonstrative assumptions, not dissertation statistics or a real business forecast.',57,139,479,'small')
C.showPage()
# P3
header(3,'Validation plan and portfolio relevance')
C.setFillColor(INK);C.setFont('Helvetica-Bold',23);C.drawString(42,H-105,'From a model to a defensible test')
para('A research-led product case study should show how a question becomes an experiment - and which claims cannot yet be made.',42,H-121,509)
box(42,H-167,510,130)
C.setFillColor(TEAL);C.setFont('Helvetica-Bold',10);C.drawString(57,H-190,'ILLUSTRATIVE EXPERIMENT DESIGN')
para('<b>Control:</b> Generic fee and ETA disclosure at checkout.<br/><b>Treatment:</b> Category/context eligibility, fee/ETA and verifiable courier-policy disclosure before checkout.<br/><b>Primary metric:</b> Completed orders / randomised eligible sessions.<br/><b>Guardrails:</b> Courier safety, complaints, delivery failures and privacy.',57,H-199,470,'small')
section_title(42,H-338,'Quality and reproducibility')
quality=[('20','JavaScript tests'),('4','Python data checks'),('7','Interactive workspaces')]
for idx,(number,label) in enumerate(quality):
 x=42+idx*175
 box(x,H-355,160,90,HexColor('#eaf1e7'))
 C.setFillColor(TEAL);C.setFont('Helvetica-Bold',28);C.drawString(x+15,H-398,number)
 C.setFont('Helvetica',8.5);C.drawString(x+15,H-421,label)
section_title(42,H-483,'Relevant roles')
para('Product Analyst &nbsp;&nbsp; • &nbsp;&nbsp; Junior Product Manager &nbsp;&nbsp; • &nbsp;&nbsp; Business Analyst &nbsp;&nbsp; • &nbsp;&nbsp; Customer Insights &nbsp;&nbsp; • &nbsp;&nbsp; UX Research &nbsp;&nbsp; • &nbsp;&nbsp; Operations Analyst',42,H-498,500,'body')
box(42,269,510,129,HexColor('#fff4ea'))
C.setFillColor(CORAL);C.setFont('Helvetica-Bold',10);C.drawString(58,247,'SOURCE & CONTRIBUTION DISCLOSURE')
para('This work was initially generated with AI assistance, based on summaries of Salonee\'s research supplied in application materials. It does not include original dissertation transcripts. She should verify the research framing and personally test, revise and understand the implementation before attributing technical development to herself.',58,233,476,'small')
para('<b>Next validation step:</b> Compare the source dissertation against the evidence ledger, confirm ethics permissions for any additional research data and replace synthetic assumptions with properly collected, consented evidence before drawing empirical conclusions.',42,119,510,'small')
C.showPage()
C.save();print(OUTPUT)
