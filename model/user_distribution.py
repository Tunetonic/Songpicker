from sqlalchemy import Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base
from database_manager import get_connection

Base = declarative_base()

class UserDistribution(Base):
    __tablename__ = "user_distribution"
    
    id = Column(Integer, Sequence("user_distribution_id_seq"), index=True, primary_key=True)
    userid = Column(String(200), unique=True, nullable=False)
    
    acoustic = Column(Float(), )
    afrobeat = Column(Float())
    alt_rock = Column(Float())
    alternative = Column(Float())
    ambient = Column(Float())
    anime = Column(Float())
    black_metal = Column(Float())
    bluegrass = Column(Float())
    blues = Column(Float())
    bossanova = Column(Float())
    brazil = Column(Float())
    breakbeat = Column(Float())
    british = Column(Float())
    cantopop = Column(Float())
    chicago_house = Column(Float())
    children = Column(Float())
    chill = Column(Float())
    classical = Column(Float())
    club = Column(Float())
    comedy = Column(Float())
    country = Column(Float())
    dance = Column(Float())
    dancehall = Column(Float())
    death_metal = Column(Float())
    deep_house = Column(Float())
    detroit_techno = Column(Float())
    disco = Column(Float())
    disney = Column(Float())
    drum_and_bass = Column(Float())
    dub = Column(Float())
    dubstep = Column(Float())
    edm = Column(Float())
    electro = Column(Float())
    electronic = Column(Float())
    emo = Column(Float())
    folk = Column(Float())
    forro = Column(Float())
    french = Column(Float())
    funk = Column(Float())
    garage = Column(Float())
    german = Column(Float())
    gospel = Column(Float())
    goth = Column(Float())
    grindcore = Column(Float())
    groove = Column(Float())
    grunge = Column(Float())
    guitar = Column(Float())
    happy = Column(Float())
    hard_rock = Column(Float())
    hardcore = Column(Float())
    hardstyle = Column(Float())
    heavy_metal = Column(Float())
    hip_hop = Column(Float())
    holidays = Column(Float())
    honky_tonk = Column(Float())
    house = Column(Float())
    idm = Column(Float())
    indian = Column(Float())
    indie = Column(Float())
    indie_pop = Column(Float())
    industrial = Column(Float())
    iranian = Column(Float())
    j_dance = Column(Float())
    j_idol = Column(Float())
    j_pop = Column(Float())
    j_rock = Column(Float())
    jazz = Column(Float())
    k_pop = Column(Float())
    kids = Column(Float())
    latin = Column(Float())
    latino = Column(Float())
    malay = Column(Float())
    mandopop = Column(Float())
    metal = Column(Float())
    metal_misc = Column(Float())
    metalcore = Column(Float())
    minimal_techno = Column(Float())
    movies = Column(Float())
    mpb = Column(Float())
    new_age = Column(Float())
    new_release = Column(Float())
    opera = Column(Float())
    pagode = Column(Float())
    party = Column(Float())
    philippines_opm = Column(Float())
    piano = Column(Float())
    pop = Column(Float())
    pop_film = Column(Float())
    post_dubstep = Column(Float())
    power_pop = Column(Float())
    progressive_house = Column(Float())
    psych_rock = Column(Float())
    punk = Column(Float())
    punk_rock = Column(Float())
    r_n_b = Column(Float())
    rainy_day = Column(Float())
    reggae = Column(Float())
    reggaeton = Column(Float())
    road_trip = Column(Float())
    rock = Column(Float())
    rock_n_roll = Column(Float())
    rockabilly = Column(Float())
    romance = Column(Float())
    sad = Column(Float())
    salsa = Column(Float())
    samba = Column(Float())
    sertanejo = Column(Float())
    show_tunes = Column(Float())
    singer_songwriter = Column(Float())
    ska = Column(Float())
    sleep = Column(Float())
    songwriter = Column(Float())
    soul = Column(Float())
    soundtracks = Column(Float())
    spanish = Column(Float())
    study = Column(Float())
    summer = Column(Float())
    swedish = Column(Float())
    synth_pop = Column(Float())
    tango = Column(Float())
    techno = Column(Float())
    trance = Column(Float())
    trip_hop = Column(Float())
    turkish = Column(Float())
    work_out = Column(Float())
    world_music = Column(Float())
    userid = Column(Float())

    def __repr__(self):
        return f"userId: {self.userid}"

engine = get_connection().get("engine")
Base.metadata.create_all(engine)