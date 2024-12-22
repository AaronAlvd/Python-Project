from app.models import db, Transcription, environment, SCHEMA
from sqlalchemy.sql import text


def seed_transcriptions():
    transcription01 = Transcription(
        user_id=1, title='Texas Centennial half dollar', 
        text="""The Texas Centennial half dollar was a commemorative fifty-cent piece struck by the United States Bureau 
        of the Mint for collectors from 1934 to 1938. It features an eagle and the Lone Star of Texas on the obverse, 
        while the reverse is a complex scene incorporating the winged goddess Victory, the Alamo Mission, and portraits of Texan founding 
        fathers Sam Houston and Stephen F. Austin, together with the Six flags over Texas. Proposed by the 
        American Legion's Texas Centennial Committee as a fundraising measure for the 100th anniversary of Texas's independence from Mexico, 
        the coin's issue was approved by Congress in 1933, ending a multi-year pause on new commemorative issues under the Hoover administration. 
        It was designed by sculptor Pompeo Coppini, previously the designer of several Texan public monuments. Rough models of the coin were 
        approved by the committee in May 1934, but rejected by the United States Commission of Fine Arts, who viewed the design as crowded and 
        overly-complicated. A compromise was reached, and the coin entered production at the Philadelphia Mint in October 1934.
        The Centennial Committee intended the coins to help finance the Texas Memorial Museum in Austin, and vended them through the American 
        Legion and banks across Texas. The vast majority of this initial, 1934-dated, issue went unsold and was sent back to the Mint to be melted 
        down for its silver. Smaller issues were produced at the Philadelphia, Denver, and San Francisco mints for the next four years, even 
        beyond the centennial itself in 1936. The Texas Centennial Committee ceased sales of the coin in November 1938. Despite the relative 
        lack of sales, the issue has proven popular with collectors, with the coins gradually appreciating in value.""")

    transcription02 = Transcription(
        user_id=1, title='Apollo 11 Moon Landing',
        text="""The Apollo 11 mission was the first manned mission to land on the Moon and safely return to Earth. 
        Launched on July 16, 1969, the spacecraft carried astronauts Neil Armstrong, Buzz Aldrin, and Michael Collins. 
        Armstrong and Aldrin became the first humans to walk on the Moon on July 20, 1969, with Armstrong famously declaring, 
        'That's one small step for [a] man, one giant leap for mankind.' The mission successfully demonstrated the United States' 
        capability to perform complex space missions and fulfilled the goal set by President John F. Kennedy in 1961 to land 
        a man on the Moon before the end of the decade. The Apollo 11 mission was a major milestone in space exploration, 
        and its success was a key event in the history of the space race between the United States and the Soviet Union.""")

    transcription03 = Transcription(
        user_id=1, title='The Great Wall of China',
        text="""The Great Wall of China is a series of fortifications made of various materials, including stone, brick, tamped earth, 
        and wood, built along the northern borders of China. The wall was constructed to protect Chinese states and empires from 
        invasions and raids by nomadic groups from the north, particularly the Mongols. The wall stretches over 13,000 miles 
        and was built over several centuries, with most of the existing wall dating back to the Ming Dynasty (1368–1644). 
        The Great Wall is considered one of the greatest architectural feats in history and is a UNESCO World Heritage Site. 
        Its construction was a monumental task that required the labor of millions of workers over many generations.""")

    transcription04 = Transcription(
        user_id=1, title='The Pyramids of Giza',
        text="""The Pyramids of Giza are a group of three ancient pyramids located in Egypt, near the city of Cairo. 
        The most famous of these is the Great Pyramid, built for the Pharaoh Khufu around 2580–2560 BCE. The pyramids were constructed 
        as tombs for the Pharaohs and are among the largest structures ever built in human history. The Great Pyramid, originally 
        standing at 481 feet, was the tallest man-made structure for over 3,800 years. These ancient monuments have long been a symbol 
        of Egypt's cultural heritage and a marvel of ancient engineering, and they continue to attract millions of tourists each year.""")    
        

    db.session.add(transcription01)
    db.session.add(transcription02)
    db.session.add(transcription03)
    db.session.add(transcription04)
    db.session.commit()



def undo_transcriptions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.transcriptions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM transcriptions"))
        
    db.session.commit()