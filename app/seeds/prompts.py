from app.models import db, Prompt, environment, SCHEMA
from sqlalchemy.sql import text

def seed_prompts():
  prompt01 = Prompt(id=1, user_id=1, prompt="""
    Title – A concise, descriptive title for the article.
    Abstract – A brief summary of the main points and findings in the artifact text.
    Introduction – A section introducing the context, background, and purpose of the research.
    Literature Review – A review of relevant existing research or historical context that aligns with the themes of the artifact.
    Methods/Approach – A description of the methodology or theoretical approach used to analyze the artifact.
    Analysis/Discussion – A detailed exploration of the artifact’s key points, with any interpretations, findings, or significant details.
    Conclusion – A summary of the implications, significance, and potential future research directions.
    References – Any sources or citations that should be included based on the information in the artifact.
    Please base the outline on the provided text, ensuring to capture the primary themes and arguments, while organizing it clearly and logically for a research paper.""")

  
  db.session.add(prompt01)
  db.session.commit()



def undo_prompts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.prompts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM prompts"))
        
    db.session.commit()