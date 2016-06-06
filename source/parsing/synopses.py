# import numpy as np
# import pandas as pd
import nltk
import re
import os
import codecs
# import mpld3
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
# from sklearn import feature_extraction


class Synopses:
    @staticmethod
    def remove_stopwords(text):
        stopwords = nltk.corpus.stopwords.words('english')

    @staticmethod
    def _remove_special_chars(text):
        text = re.sub(r'\W+', ' ', text)
        return text

    @staticmethod
    def _trim_white_spaces(text):
        return " ".join(text.split())

    @staticmethod
    def _tokenize_and_stem(text):
        stemmer = SnowballStemmer("english")
        tokens = [word for sent in nltk.sent_tokenize(text) for word in
                  nltk.word_tokenize(sent)]
        filtered_tokens = []
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        return stems

    @staticmethod
    def make(text):
        text = Synopses._remove_special_chars(text)
        print('({0})_remove_special_chars:\t\t{1}'.format(len(text.split()),
                                                          text))

        text = Synopses._trim_white_spaces(text)
        print('({0})_trim_white_spaces:\t\t\t{1}'.format(len(text.split()),
                                                         text))

        text = Synopses._tokenize_and_stem(text)
        print('({0}) _tokenize_and_stem:\t\t{1}'.format(len(text), text))
        return text

if __name__ == '__main__':
    text = """
        {{monththisyear|4}}
        '''April''' is the fourth [[month]] of the [[year]], and comes between [[March]] and [[May]]. It has 30 [[day]]s. April begins on the same day of week as [[July]] in all years and also [[January]] in leap years.

        April's [[flower]]s are the [[Sweet Pea]] and [[Asteraceae|Daisy]]. Its [[birthstone]] is the [[diamond]]. The meaning of the diamond is innocence.

        == The Month ==
        [[File:Colorful spring garden.jpg|thumb|180px|right|[[Spring]] flowers in April in the [[Northern Hemisphere]].]]
        April comes between [[March]] and [[May]], making it the fourth month of the year. It also comes first in the year out of the four months that have 30 days, as [[June]], [[September]] and [[November]] are later in the year. It starts on the same day of the week as [[July]] every year, and starts on the same day as [[January]] in [[leap year]]s. In a [[common year]], April starts on the same day of the week as [[October]] of the previous year, and in [[leap year]]s starts on the same day as [[May]] of the previous year.
        April ends on the same day of the week as [[December]] every year. In a [[common year]], it ends on the same day as [[July]] of the previous year. In a [[leap year]], it ends on the same day as [[October]] of the previous year.

        April is a [[spring]] month in the [[Northern Hemisphere]] and an [[autumn|autumn/fall]] month in the [[Southern Hemisphere]]. In each [[hemisphere]], it is the [[season]]al equivalent of [[October]] in the other.

        It is unclear as to where April got its name. A common theory is that it comes from the [[Latin]] word "aperire", meaning "to open", referring to [[flower]]s opening in [[spring]]. Another theory is that the name could come from [[Aphrodite]], the Greek goddess of [[love]]. It was originally the second month in the old Roman [[Calendar]], before the start of the new year was put to [[January 1]].

        Quite a few festivals are held in this month. In many [[Southeast Asia]]n cultures, new year is celebrated in this month (including [[Songkran]]). In Western [[Christianity]], [[Easter]] can be celebrated on a [[Sunday]] between [[March 22]] and [[April 25]]. In [[Eastern Orthodox Church|Orthodox]] Christianity, it can fall between [[April 4]] and [[May 8]]. At the end of the month, Central and Northern [[Europe]]an [[culture]]s celebrate [[Walpurgis Night]] on [[April 30]], marking the transition from [[winter]] into [[summer]].

        == April in poetry ==
        [[poetry|Poets]] use ''April'' to mean the end of winter. For example: ''April showers bring [[May]] flowers.''

        == Events in April ==
        === Fixed Events ===
        [[File:Aprilsnar 2001.png|thumb|200px|right|An [[April Fools' Day]] hoax for [[April 1]] in [[Copenhagen]].]]
        [[File:Songkran in Wat Kungthapao 03.jpg|thumb|180px|right|[[Songkran]] celebration in [[Thailand]] around [[April 14]].]]
        [[File:Earth flag PD.jpg|thumb|200px|right|Proposed [[flag]] for [[Earth Day]] on [[April 22]].]]
        [[File:St George's Day 2010 - 14.jpg|thumb|200px|right|[[Saint George]]'s Day on [[April 23]] in [[London]]'s [[Trafalgar Square]].]]
        [[File:Anzac1.JPG|thumb|180px|right|[[ANZAC Day]] commemoration in [[Australia]] on [[April 25]].]]
        [[File:Koninginnedag2007.jpg|thumb|180px|right|Queen's Day, [[April 30]], celebration in the [[Netherlands]]. It changed to King's Day, [[April 27]], in [[2014]].]]
        [[File:Valborgsbrasa-1.jpg|thumb|210px|right|[[Walpurgis Night]] bonfire on [[April 30]] in [[Sweden]].]]
        * [[April 1]] - [[April Fools' Day]]
        * [[April 1]] - Islamic Republic Day ([[Iran]])
        * [[April 2]] - International Children's Book Day
        * [[April 2]] - [[Thailand|Thai]] Heritage and [[wikt:conservation|Conservation]] Day
        * [[April 2]] - World [[Autism]] Awareness Day
        * [[April 2]] - Malvinas Day ([[Argentina]])
        * [[April 4]] - Independence Day ([[Senegal]])
        * [[April 4]] - International Day for Landmine Awareness and Assistance
        * [[April 4]] - Peace Day ([[Angola]])
        * [[April 5]] - End of [[Tax]] Year ([[United Kingdom]])
        * [[April 6]] - Tartan Day ([[Canada]] and [[United States]])
        * [[April 6]] - Chakri Day ([[Thailand]])
        * [[April 7]] - Day of Maternity and Beauty ([[Armenia]])
        * [[April 7]] - Genocide Memorial Day ([[Rwanda]])
        * [[April 7]] - World [[Health]] Day
        * [[April 7]] - Women's Day ([[Mozambique]])
        * [[April 8]] - [[Buddha]]'s Birthday ([[Buddhism]])
        * [[April 9]] - Martyrs' Day ([[Tunisia]])
        * [[April 9]] - Day of National Unity ([[Georgia (country)|Georgia]])
        * [[April 9]] - Day of the [[Finnish language]]
        * [[April 12]] - [[Cosmonaut]]s' Day ([[Russia]]), marking the day of [[Yuri Gagarin]]'s space flight
        * [[April 13]] - Songkan ([[Laos]]), local New Year celebration
        * [[April 13]] - [[Cambodia]]n New Year
        * [[April 13]] - [[Thomas Jefferson]]'s [[Birthday]] ([[United States]])
        * [[April 14]] - [[Southeast Asia]]n [[New Year]] festivals, including [[Songkran]]
        * [[April 14]] - [[Georgian language]] Day
        * [[April 14]] - Youth Day ([[Angola]])
        * [[April 14]] - Ambedkar Tayanti ([[India]])
        * [[April 14]] - Pan-American Day
        * [[April 15]] - [[Tax]] Day ([[United States]])
        * [[April 15]] - [[Kim Il-Sung]]'s [[Birthday]] ([[North Korea]])
        * [[April 15]] - [[Father Damien]] Day ([[Hawaii]])
        * [[April 15]] - [[Jackie Robinson]] Day ([[Major League Baseball]])
        * [[April 16]] - [[Birthday]] of Queen [[Margrethe II of Denmark]]
        * [[April 16]] - Emancipation Day ([[Washington, DC]])
        * [[April 16]] - World [[Voice]] Day
        * [[April 16]] - [[Selena]] Day ([[Texas]])
        * [[April 17]] - National Day of [[Syria]]
        * [[April 17]] - Flag Day ([[American Samoa]])
        * [[April 17]] - Women's Day ([[Gabon]])
        * [[April 17]] - World [[Hemophilia]] Day
        * [[April 18]] - Independence Day ([[Zimbabwe]])
        * [[April 18]] - Invention Day ([[Japan]])
        * [[April 18]] - International Day of [[Monument]]s and Sites
        * [[April 19]] - [[Bicycle]] Day
        * [[April 19]] - Dutch-American Friendship Day
        * [[April 19]] - [[Birthday]] of King [[Mswati III]] of [[Swaziland]]
        * [[April 19]] - Patriots' Day ([[Massachusetts]], [[Maine]], [[Wisconsin]])
        * [[April 20]] - 4/20 in [[Cannabis]] [[Culture]]
        * [[April 21]] - [[John Muir]] Day ([[California]])
        * [[April 21]] - San Jacinto Day ([[Texas]])
        * [[April 21]] - Kartini Day ([[Indonesia]])
        * [[April 21]] - National [[Tree]] Planting Day ([[Kenya]])
        * [[April 21]] - First Day of [[Ridran]] ([[Baha'i]] faith)
        * [[April 21]] - Grounation Day ([[Rastafari movement]])
        * [[April 22]] - [[Earth Day]]
        * [[April 22]] - Discovery Day ([[Brazil]])
        * [[April 23]] - [[Saint George]]'s Day, celebrating the patron saint of several countries, regions and cities (including [[England]] and [[Catalonia]])
        * [[April 23]] - World [[Book]] Day
        * [[April 23]] - National Sovereignty and [[Child]]ren's Day ([[Turkey]])
        * [[April 24]] - Democracy Day ([[Nepal]])
        * [[April 24]] - Genocide Day ([[Armenia]])
        * [[April 24]] - [[Republic]] Day (the [[Gambia]])
        * [[April 25]] - [[Australia]] and [[New Zealand]] celebrate [[ANZAC Day]]. [http://www.awm.gov.au/dawn/spirit/meaning.asp ANZAC] means Australian and New Zealand Army Corps, and began in 1915.
        * [[April 25]] - World [[DNA]] Day
        * [[April 25]] - World [[Malaria]] Day
        * [[April 25]] - Flag Day ([[Swaziland]], [[Faroe Islands]])
        * [[April 25]] - Freedom Day ([[Portugal]])
        * [[April 25]] - Liberation Day ([[Italy]])
        * [[April 25]] - Army Day ([[North Korea]])
        * [[April 26]] - Union Day ([[Tanzania]])
        * [[April 26]] - Confederate Memorial Day ([[Texas]], [[Florida]])
        * [[April 27]] - Independence Day ([[Sierra Leone]] and [[Togo]])
        * [[April 27]] - Freedom Day ([[South Africa]])
        * [[April 27]] - World [[Tapir]] Day
        * [[April 27]] - King's Day ([[Netherlands]]) from [[2014]], birthday of [[Willem-Alexander of the Netherlands]]
        * [[April 28]] - Workers Memorial Day
        * [[April 28]] - National Day ([[Sardinia]])
        * [[April 28]] - National Heroes Day ([[Barbados]])
        * [[April 29]] - Showa Day ([[Japan]]), birthday of Emperor [[Hirohito]], who died in [[1989]]
        * [[April 29]] - International [[Dance]] Day
        * [[April 30]] - Former Queen's Day Holiday in the [[Netherlands]] (changed to King's Day, [[April 27]] in [[2014]]), was the birthday of former Queen [[Juliana of the Netherlands]]
        * [[April 30]] - Flag Day in [[Sweden]] (birthday of King [[Carl XVI Gustaf of Sweden]])
        * [[April 30]] - International [[Jazz]] Day
        * [[April 30]] - [[Walpurgis Night]] (Central and Northern [[Europe]])

        === Moveable Events ===
        [[File:Vajicka1.jpg|thumb|200px|right|Eggs celebrating [[Easter]], which often falls in April, but sometimes falls in [[March]].]]
        [[File:Aprilregen - Lithografie.jpg|thumb|200px|right|Image traditionally showing it as [[rain]]ing in April in the [[Northern Hemisphere]].]]
        * [[Easter]]-related events in Western [[Christianity]]:
        **Palm Sunday (between [[March 15]] and [[April 18]])
        **Maundy Thursday (between [[March 19]] and [[April 22]])
        **Good Friday (between [[March 20]] and [[April 23]])
        **[[Easter]] Sunday (between [[March 22]] and [[April 25]])
        **Easter Monday (between [[March 23]] and [[April 26]])
        * Eastern Orthodox Easter falls between [[April 4]] and [[May 8]].
        * Ascension Day (Western Christianity), falls between [[April 30]] and [[June 3]].
        * [[Judaism|Jewish]] [[Passover]] - falls in the same week as Western [[Christianity]]'s [[Holy Week]], which is the week leading up to [[Easter]].
        * [[Mother's Day]] ([[UK]]) falls between [[March 1]] and [[April 4]].
        * World [[Snooker]] Championship (late April, early [[May]])
        * [[Horse racing]] - [[Grand National]] ([[UK]]), [[Kentucky Derby]] ([[United States]])
        * Start of [[Daylight Saving Time]] - Clocks going forward one hour:
        **Most of [[Mexico]]
        **[[Morocco]] ([[Ramadan]] does not include Daylight Saving Time)
        * End of [[Daylight Saving Time]] - Clocks going back one hour:
        **Southeast [[Australia]], and [[New Zealand]]
        **[[Chile]]
        * [[Marathon]] Events in the following cities:
        **[[Belgrade]], [[Serbia]]
        **[[Boston, Massachusetts]], [[United States]]
        **[[Brighton]], [[United Kingdom]]
        **[[Enschede]], [[Netherlands]]
        **[[London]], [[United Kingdom]]
        **[[Madrid]], [[Spain]]
        **[[Paris]], [[France]]
        **[[Rotterdam]], [[Netherlands]]
        **[[Utrecht (city)|Utrecht]], [[Netherlands]]
        **[[Zurich]], [[Switzerland]]

        == Selection of Historical Events ==
        [[File:Nunavut-Feierlichkeit (01-04-99).jpg|thumb|180px|right|[[Inauguration]] celebration for [[Nunavut]] on [[April 1]], [[1999]].]]
        [[File:Moai Rano raraku.jpg|thumb|160px|right|A statue on [[Easter Island]] - Jacob Roggeveen became the first [[Europe]]an to land there on [[April 5]], [[1722]].]]
        [[File:Titanic-New York Herald front page.jpeg|thumb|150px|right|[[Newspaper]] report on the sinking of the [[RMS Titanic]] on [[April 15]], [[1912]].]]
        [[File:San Francisco Fire Sacramento Street 1906-04-18.jpg|thumb|180px|right|[[Fire]]s after the [[San Francisco]] [[earthquake]] on [[April 18]], [[1906]].]]
        [[File:Anzac Beach 4th Bn landing 8am April 25 1915.jpg|thumb|180px|right|[[Australia]]n and [[New Zealand]] forces landing at Anzac Cove, [[April 25]], [[1915]].]]
        [[File:HMS Bounty.jpg|thumb|200px|right|Painting showing the Mutiny on the Bounty on [[April 28]], [[1789]].]]
        [[File:Juliana 1963.jpg|thumb|150px|right|Queen [[Juliana of the Netherlands]], who abdicated the throne on her 71st [[birthday]], [[April 30]], [[1980]].]]
        * [[April 1]], [[1918]] - The [[Royal Air Force]] is founded.
        * [[April 1]], [[1976]] - [[Apple Inc.]] is founded.
        * [[April 1]], [[1979]] - The [[Islamic Republic of Iran]] is founded.
        * [[April 1]], [[1999]] - The [[territory]] of [[Nunavut]] is created in Northern [[Canada]].
        * [[April 1]], [[2001]] - The [[Netherlands]] introduces [[same-sex marriage]], as the first [[country]] to do so.
        * [[April 2]], [[1519]] - [[Florida]] is sighted by a [[Europe]]an for the first time.
        * [[April 2]], [[1930]] - [[Haile Selassie]] becomes [[Emperor of Ethiopia]].
        * [[April 2]], [[1982]] - Start of the [[Falklands War]], as Argentine forces land on the [[Falkland Islands]].
        * [[April 2]], [[2005]] - [[Pope John Paul II]] dies aged 84, after 26-and-a-half years as [[Pope]].
        * [[April 3]], [[1973]] - The first-ever [[mobile phone]] call is placed by Martin Cooper in [[New York City]].
        * [[April 4]], [[1721]] - [[Robert Walpole]] becomes the first [[Prime Minister]] of [[Great Britain]].
        * [[April 4]], [[1841]] - [[William Henry Harrison]] dies. He was [[President of the United States]] for 31 days, the shortest-ever time in office for a US President.
        * [[April 4]], [[1960]] - [[Senegal]] becomes independent.
        * [[April 4]], [[1968]] - [[Assassination]] of [[Martin Luther King, Jr.]] in [[Memphis, Tennessee]].
        * [[April 5]], [[1722]] - [[Jacob Roggeveen]] becomes the first [[Europe]]an to land on [[Easter Island]], landing there on [[Easter]] Sunday.
        * [[April 6]], [[1320]] - [[Scotland]]'s independence is confirmed with the Declaration of [[Arbroath]].
        * [[April 6]], [[1830]] - The [[Mormonism|Mormon]] Church is founded.
        * [[April 6]], [[1909]] - [[Robert Peary]] claims to have been first at the [[North Pole]] on this date.
        * [[April 7]], [[1994]] - The [[Rwandan Genocide]] begins.
        * [[April 9]], [[1865]] - [[American Civil War]]: [[Confederate States of America|Confederate]] forces under [[Robert E. Lee]] surrender to Union forces.
        * [[April 9]], [[1940]] - [[World War II]]: [[Denmark]] and [[Norway]] are invaded by [[Nazi]] [[Germany]].
        * [[April 9]], [[1989]] - April 9 tragedy: In [[Tbilisi]], [[Georgia (country)|Georgia]], a peaceful demonstration for independence is broken up by the [[Soviet]] [[Army]], killing 20 people. The country gains independence on this date exactly two years later.
        * [[April 10]], [[1815]] - Mount [[Tambora]] in [[Indonesia]] erupts in a huge eruption, affecting the world's climate for at least a year.
        * [[April 10]], [[2010]] - A [[fixed-wing aircraft|plane]] crash near Smolensk, [[Russia]], kills several people who were important in [[Poland]], including [[President]] [[Lech Kaczynski]].
        * [[April 11]], [[1814]] - [[Napoleon Bonaparte]] is [[exile]]d to the [[island]] of [[Elba]].
        * [[April 11]], [[1954]] - Said to have been the most boring day of the [[20th century]].
        * [[April 12]], [[1861]] - The [[American Civil War]] begins at Fort Sumter, [[South Carolina]].
        * [[April 12]], [[1945]] - US President [[Franklin D. Roosevelt]] dies, and [[Harry S. Truman]] replaces him.
        * [[April 12]], [[1961]] - [[Yuri Gagarin]] becomes the first [[human]] to fly into [[Outer space|space]].
        * [[April 14]], [[1865]] - US President [[Abraham Lincoln]] is shot dead at Ford's Theatre by [[John Wilkes Booth]]. Lincoln dies the next day.
        * [[April 14]], [[2010]] - [[Qinghai]] Province, [[China]], is hit by an [[earthquake]], killing tens of thousands of people.
        * [[April 14]], [[2010]] - The eruption of [[Eyjafjallajokull]] in [[Iceland]] shuts down air traffic around [[Europe]] for a week, due to its ash cloud.
        * [[April 15]], [[1912]] - The [[ship]] [[RMS Titanic]] sinks near [[Newfoundland]] after hitting an iceberg, resulting in the deaths of many of the people on board.
        * [[April 16]], [[1943]] - [[Albert Hofmann]] discovers [[LSD]]'s effects.
        * [[April 17]], [[1946]] - [[Syria]] gains full independence from [[France]].
        * [[April 18]], [[1906]] - [[1906 San Francisco earthquake]]: [[San Francisco]], [[California]], is hit by a big [[earthquake]], resulting in [[fire]]s that destroy large parts of the city.
        * [[April 18]], [[1980]] - [[Zimbabwe]] gains full independence.
        * [[April 19]], [[1897]] - The first [[Boston Marathon]] is held.
        * [[April 19]], [[1971]] - [[Sierra Leone]] becomes a [[republic]].
        * [[April 19]], [[1993]] - The siege of the Branch Davidians at Waco, [[Texas]], ends in a fire that kills 82 people.
        * [[April 19]], [[1995]] - [[Timothy McVeigh]] carries out the [[Oklahoma City bombing]], killing 169 people.
        * [[April 19]], [[2005]] - Joseph Alois Ratzinger becomes [[Pope Benedict XVI]].
        * [[April 20]], [[1902]] - [[Marie Curie]] and [[Pierre Curie]] refine [[Radium]].
        * [[April 20]], [[2010]] - [[Deepwater Horizon oil spill]]: A massive fire on the Deepwater Horizon drilling rig in the [[Gulf of Mexico]] kills 11 workers and causes a massive [[oil]] spill, the worst spill in US history.
        * [[April 21]], [[753 BC]] - Legendary founding date of [[Rome]]
        * [[April 21]], [[1509]] - [[Henry VIII of England]] becomes [[King]].
        * [[April 21]], [[1908]] - [[Frederick Cook]] claims to have reached the [[North Pole]] on this date.
        * [[April 22]], [[1502]] - [[Pedro Alvares Cabral]] becomes the first [[Europe]]an to reach present-day [[Brazil]].
        * [[April 22]], [[1970]] - [[Earth Day]] is observed for the first time.
        * [[April 23]], [[1533]] - The [[Church of England]] declares that [[Henry VIII of England]] and [[Catherine of Aragon]] are not married.
        * [[April 24]], [[1916]] - The [[Easter Rising]] occurs in [[Dublin]], [[Ireland]].
        * [[April 24]], [[1990]] - The [[Hubble Space Telescope]] is launched on the [[Space Shuttle Discovery]].
        * [[April 25]], [[1915]] - [[World War I]]: In [[Turkey]], the [[Battle of Gallipoli]] begins, [[Australia]]n, French, British and [[New Zealand]] forces land at Anzac cove.
        * [[April 25]], [[1974]] - [[Portugal]]'s dictatorship is overthrown in a coup, in what is known as the Carnation Revolution.
        * [[April 26]], [[1937]] - [[Spanish Civil War]]: German planes bomb the town of Guernica, [[Basque Country]], later depicted in a painting by [[Pablo Picasso]].
        * [[April 26]], [[1964]] - [[Tanganyika]] and [[Zanzibar]] merge to form [[Tanzania]].
        * [[April 26]], [[1986]] - A reactor explosion occurs at the [[Chernobyl]] nuclear plant in present-day [[Ukraine]], with [[radiation]] spreading around Europe and the world.
        * [[April 26]]/[[April 27|27]], [[1994]] - [[South Africa]] holds its first free elections.
        * [[April 27]], [[1960]] - [[Togo]] becomes independent from [[France]].
        * [[April 27]], [[1961]] - [[Sierra Leone]] becomes independent from the [[United Kingdom]].
        * [[April 28]], [[1789]] - Mutiny on the ship Bounty in the [[Pacific Ocean]], lead by [[Fletcher Christian]].
        * [[April 28]], [[1945]] - [[Benito Mussolini]] is executed by Italian partisans.
        * [[April 28]], [[1947]] - In [[Peru]], [[Thor Heyerdahl]] starts his [[Kon-Tiki]] expedition aimed at proving his theory that the [[Polynesia]]n settlers on the [[Pacific Ocean]]'s [[island]]s came from [[South America]].
        * [[April 29]], [[1991]] - A [[cyclone]] in [[Bangladesh]] kills an estimated 138,000 people.
        * [[April 29]], [[2011]] - The wedding of [[Prince William, Duke of Cambridge]] and [[Catherine, Duchess of Cambridge]] is broadcast worldwide.
        * [[April 30]], [[1789]] - [[George Washington]] becomes the first [[President of the United States]].
        * [[April 30]], [[1803]] - The [[United States]] purchases (buys) the [[Louisiana]] territory from [[France]].
        * [[April 30]], [[1945]] - [[Adolf Hitler]] commits suicide on the same day that the [[Soviet]] Army raises the Red Flag on [[Berlin]]'s [[Reichstag]].
        * [[April 30]], [[1952]] - The [[Diary]] of [[Anne Frank]] is published in English.
        * [[April 30]], [[1975]] - The [[Vietnam War]] ends, as [[North Vietnam]]ese forces take [[Saigon]].
        * [[April 30]], [[1980]] - Queen [[Juliana of the Netherlands]] abdicates the throne, and her daughter becomes Queen [[Beatrix of the Netherlands]]. Beatrix later also abdicates, on this day in [[2013]], in favor of her son, King [[Willem-Alexander of the Netherlands]].
        {{-}}

        == Trivia ==
        [[File:Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg|thumb|150px|right|[[Elizabeth II]] is one of six current [[Europe]]an [[monarch]]s to have been born in April.]]
        * In Western [[Christianity]], there is a bigger likelihood of [[Easter]] falling in April than in [[March]].
        * The months around April ([[March]] and [[May]]) both start with an 'M' in the [[English language]], with an 'A' as the second letter.
        * In the [[English language]], April is the first of three months in-a-row, along with [[May]] and [[June]], that is also a [[female]] given name.
        * The astrological signs for April are [[Aries]] ([[March 21]] to [[April 20]]) and [[Taurus]] ([[April 21]] to [[May 21]]).
        * The [[sweet pea]] and [[Asteraceae|daisy]] are the traditional birth flowers for April.
        * Birthstone for April is the [[Diamond]].
        * If the months of the [[year]] were arranged in [[alphabet]]ical order in the [[English language]], April would come first.
        * Six current [[Europe]]an [[monarch]]s were born in April. They are King [[Philippe of Belgium]] ([[April 15]]), Queen [[Margrethe II of Denmark]] ([[April 16]]), [[Henri, Grand Duke of Luxembourg]] ([[April 16]]), [[Elizabeth II]] of the [[United Kingdom]] and [[Commonwealth realm]]s ([[April 21]]), King [[Willem-Alexander of the Netherlands]] ([[April 27]]), and King [[Carl XVI Gustaf of Sweden]] ([[April 30]]).
        {{-}}

        {{Months}}
        """
    ts = Synopses.make(text[:500])

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                       min_df=0.2, stop_words='english',
                                       use_idf=True,
                                       tokenizer=Synopses.make,
                                       ngram_range=(1, 3))

    # tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)

    # print(tfidf_matrix.shape)
