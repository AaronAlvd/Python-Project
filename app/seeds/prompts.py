from app.models import db, Prompt, environment, SCHEMA
from sqlalchemy.sql import text

def seed_prompts():
  prompt01 = Prompt(id=1, user_id=1, prompt="""
  Writing Prompt for an Article: "The Impact of Technology on Human Connection" As technology continues to advance, it's becoming increasingly 
  integrated into our daily lives, transforming the way we interact with the world and with each other. In what ways has technology enhanced 
  our ability to stay connected with others, especially those far away? Has it improved communication, or has it led to a rise in isolation 
  and disconnection? How do platforms like social media, messaging apps, and video calls affect the quality of our relationships? Are we replacing 
  face-to-face interactions with digital ones, and if so, what impact does this have on emotional intimacy? On the flip side, how has technology
  made it possible for people to connect in ways that were once impossible, such as in long-distance relationships or with people who share niche 
  interests? Are there any drawbacks to this, and could we be at risk of losing certain forms of connection that are important for our well-being?
  """)

  prompt02 = Prompt(id=2, user_id=1, prompt="""
  "The Mysterious Letter": One rainy afternoon, you receive an envelope with no return address, just your name written in a familiar handwriting 
  that you can’t quite place. Inside, there’s a single letter, and as you begin to read, you’re filled with an unsettling sense of deja vu. The 
  letter mentions things only you would know—events from your childhood, your greatest fears, and even your deepest secrets. But who would know 
  these things about you? And why now, after all these years? Is someone watching you, or is this a cruel prank? The letter ends with a chilling 
  question: “Will you go back to where it all began?” What is the "beginning" the letter refers to, and what would happen if you decided to revisit 
  it? Could this letter be the key to unraveling an old mystery, or is it something far more dangerous than you ever expected?
  """)

  db.session.add(prompt01)
  db.session.add(prompt02)
  db.session.commit()



def undo_prompts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.prompts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM prompts"))
        
    db.session.commit()