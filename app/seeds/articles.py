from app.models import Article, db, SCHEMA, environment
from sqlalchemy.sql import text

def seed_articles():
  article01 = Article(id=1, user_id=1, slug='high-court-of-1920',
    text="""Judicial Administration and Governance in Tanganyika: The Special Tribunal and High Court Notices of 1920

    In the aftermath of World War I, Tanganyika transitioned to British administration under the League of Nations Mandate. This period saw significant legal and administrative reforms as the British sought to establish effective governance structures in the territory. Among these changes, the establishment of the Special Tribunal and the operational framework of the High Court in 1920 offer valuable insights into the judicial priorities and constraints of the era.
    
    The Establishment of the Special Tribunal
    The Special Official Gazette of December 1920 detailed the establishment and functioning of the Special Tribunal, an institution tasked with handling civil cases under the Courts Ordinance of 1920. A key provision in these reforms was the delegation of civil jurisdiction to Resident Magistrates and District Political Officers. They were empowered to preside over cases where the claim did not exceed Fls. 1500, allowing for decentralized justice in rural and administrative regions.
    
    Judge W.M. Morris Carter, the presiding authority of the Special Tribunal, emphasized this delegation in his directive, citing the necessity of efficient dispute resolution. Additionally, the Gazette specified an appeals mechanism, ensuring that judgments made by Resident Magistrates or District Political Officers could be reviewed by the Judge of the Special Tribunal or a Judge of the High Court. This dual-layered system reflects an effort to balance accessibility to justice with the preservation of oversight by higher courts.
    
    Challenges in Judicial Operations
    Despite these administrative strides, the judicial system faced notable operational challenges. The Gazette explicitly mentioned constraints on the High Court due to a lack of clerical staff. To address these limitations, the judiciary prioritized urgent civil cases and those requiring specific judicial actions, such as arrest of defendants or attachment of property before judgment. This prioritization underscores the difficulties of implementing a fully functional legal system amidst resource shortages.
    
    The notices also reveal the judiciary's reliance on interim measures to maintain operations. For example, urgent cases could only proceed with certification from a Judge as being of pressing importance. This approach, while pragmatic, highlights the strained administrative capacity of the nascent judicial system in Tanganyika.
    
    Judicial Appointments and Administrative Refinements
    Another significant aspect of these notices was the announcement of key judicial appointments. W.A. Wilson, the Registrar of the High Court, was appointed Registrar of the Special Tribunal, while J.Q. Hanrahan assumed the role of Deputy Registrar. These appointments were integral to establishing the administrative framework of the Special Tribunal, ensuring that judicial processes could proceed with proper documentation and oversight.
    
    The Gazette also included a corrigendum, rectifying a date in Ordinance No. 9 of 1920, which demonstrates the iterative nature of legal and administrative reforms during this period. Such corrections reflect the challenges of implementing complex governance systems in a transitioning colony.
    
    Implications and Significance
    The establishment of the Special Tribunal and the operational constraints of the High Court provide a snapshot of British governance priorities in Tanganyika during the early 1920s. The delegation of judicial authority aimed to extend access to justice across the territory while addressing the limitations of centralized administration. However, the emphasis on urgent cases and the reliance on temporary measures reveal the practical difficulties of building a functional legal system in a resource-constrained environment.
    
    These developments also highlight the broader colonial strategy of balancing efficiency with oversight. By empowering local magistrates while retaining appellate mechanisms, the British sought to maintain both administrative efficiency and judicial integrity. The appointments of key officials further underline the importance of skilled personnel in achieving these goals.
    
    Conclusion
    The judicial notices from December 1920 serve as valuable artifacts of colonial administration in Tanganyika. They illustrate how legal frameworks were adapted to meet the unique challenges of governing a mandated territory. The Special Tribunal and High Court not only reflect the judicial priorities of the time but also reveal the resource and administrative constraints faced by colonial authorities. Future research could explore comparative analyses with other British territories to better understand the broader implications of these governance strategies.
    
    By examining these historical records, we gain deeper insight into the complex interplay between colonial legal systems, administrative challenges, and the evolving nature of governance in post-World War I East Africa.""")

  db.session.add(article01)
  db.session.commit()

def undo_articles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.articles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM articles"))
        
    db.session.commit()
