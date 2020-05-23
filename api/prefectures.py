from prefectures_data import *

japan = {
    "name": "Nippon",
    "islands-number": "6,852",
    "capital": "Tōkyō",
    "population": f"{japan_population}",
    "density": f"{japan_density}",
    "density-mi": f"{japan_density_mi}",
    "emperor": f"{japan_emperor}",
    "prime-minister": f"{japan_minister}",
    "gdp-ppp": f"{gdp_ppp}, By head: {gdp_ppp_per}",
    "gdp-nominal": f"{gdp_nom}, By head: {gdp_nom_per}",
    "driving-side": "left",
    "national-language": "Japanese",
    "area": "377,975 km2",
    "currency": "Japanese yen (¥) (JPY)",
    "time-zone": "UTC+09:00 (JST)",
    "calling-code": "+81",
    "iso-code": "JP",
    "area-mi": "145,937 sq mi",
    "climate": "Predominantly temperate",
    "local-dishes": ['Sushi', 'Sashimi', 'Ramen', 'Onogiri', 'Nabe', 'Miso', 'Tempura', 'Soba', 'Yakitori', 'Kaiseki', 'Udon', 'Sukiyaki', 'Tonkatsu', 'Donburi', 'Curry'],
    "economy": ['Industry', 'Agriculture', 'Fishery', 'Services', 'Tourism', 'Science and Technology'],
    "name-kanji": "日本国",
    "capital-kanji": "東京都",
}

hokkaido = {
    "name": "Hokkaido",
    "region": "Hokkaido",
    "island": "Hokkaido",
    "capital": "Sapporo",
    "population": f"{hokkaido_population}",
    "density": f"{hokkaido_density}",
    "density-mi": f"{hokkaido_density_mi}",
    "area": "83,423.84 km2",
    "area-mi": "32,210.12 sq mi",
    "climate": "Humid continental",
    "local-dishes": ['Kaisen-don', 'Jingisukan', 'Uni, Ikura-don', 'Ishikari Nabe', 'Nama Uni Donburi', 'Chan Chan Yaki'],
    "economy": ['Light industry', 'Agriculture', 'Aquaculture', 'Forestry', 'Coal mining'],
    "name-kanji": "北海道",
    "capital-kanji": "札幌市",
    "iso-code": "JP-01",
    "area-code": "011–016"
}

aomori = {
    "name": "Aomori",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Aomori",
    "population": f"{aomori_population}",
    "density": f"{aomori_density}",
    "density-mi": f"{aomori_density_mi}",
    "area": "9,645.64 km2",
    "area-mi": "3,724.20 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Ichigoni', 'Senbei Jiru', 'Ooma Maguro'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name-kanji": "青森県",
    "capital-kanji": "青森市",
    "iso-code": "JP-02",
    "area-code": "017"
}

iwate = {
    "name": "Iwate",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Morioka",
    "population": f"{iwate_population}",
    "density": f"{iwate_density}",
    "density-mi": f"{iwate_density_mi}",
    "area": "15,275.01 km2",
    "area-mi": "5,897.71 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Morioka Reimen', 'Morioka Jajamen', 'Wanko Soba'],
    "economy": ['Communications manufacturing', 'Animal husbandry', 'Aquaculture'],
    "name-kanji": "岩手県",
    "capital-kanji": "盛岡市",
    "iso-code": "JP-03",
    "area-code": "019"
}

miyagi = {
    "name": "Miyagi",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Sendai",
    "population": f"{miyagi_population}",
    "density": f"{miyagi_density}",
    "density-mi": f"{miyagi_density_mi}",
    "area": "7,282.22 km2",
    "area-mi": "2,811.68 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Gyuutan Yaki', 'Zundamochi', 'Kaki Ryori'],
    "economy": ['Fishery', 'Agriculture', 'Electronics', 'Appliances', 'Food Processing'],
    "name-kanji": "宮城県",
    "capital-kanji": "仙台市",
    "iso-code": "JP-04",
    "area-code": "022"
}

akita = {
    "name": "Akita",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Akita",
    "population": f"{akita_population}",
    "density": f"{akita_density}",
    "density-mi": f"{akita_density_mi}",
    "area": "11,637.52 km2",
    "area-mi": "4,493.27 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kiritanpo Nabe', 'Inaniwa Udon', 'Hata Hata Zushi'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name-kanji": "秋田県",
    "capital-kanji": "秋田市",
    "iso-code": "JP-05",
    "area-code": "018"
}

yamagata = {
    "name": "Yamagata",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Yamagata",
    "population": f"{yamagata_population}",
    "density": f"{yamagata_density}",
    "density-mi": f"{yamagata_density_mi}",
    "area": "9,325.15 km2",
    "area-mi": "3,600.46 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Imo Nabe', 'Tamago Konyaku', 'Dongara Jiru'],
    "economy": ['Fruit growing'],
    "name-kanji": "山形県",
    "capital-kanji": "山形市",
    "iso-code": "JP-06",
    "area-code": "023"
}

fukushima = {
    "name": "Fukushima",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Fukushima",
    "population": f"{fukushima_population}",
    "density": f"{fukushima_density}",
    "density-mi": f"{fukushima_density_mi}",
    "area": "13,783.90 km2",
    "area-mi": "5,321.99 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kozuyu', 'Kenchin Udon', 'Nishin no Sanshou Zuke'],
    "economy": ['Fishery', 'Agriculture', 'Electric industry', 'Nuclear power'],
    "name-kanji": "福島県",
    "capital-kanji": "福島市",
    "iso-code": "JP-07",
    "area-code": "024"
}

ibaraki = {
    "name": "Ibaraki",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Mito",
    "population": f"{ibaraki_population}",
    "density": f"{ibaraki_density}",
    "density-mi": f"{ibaraki_density_mi}",
    "area": "6,097.19 km2",
    "area-mi": "2,354.14 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Ankou Nabe', 'Ankou no Dobu Jiru', 'Kenchin Jiru'],
    "economy": ['Agriculture', 'Nuclear energy', 'Machining industry'],
    "name-kanji": "茨城県",
    "capital-kanji": "水戸市",
    "iso-code": "JP-08",
    "area-code": "029"
}

tochigi = {
    "name": "Tochigi",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Utsunomiya",
    "population": f"{tochigi_population}",
    "density": f"{tochigi_density}",
    "density-mi": f"{tochigi_density_mi}",
    "area": "6,408.09 km2",
    "area-mi": "2,474.18 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Shimotsukare', 'Gyouza', 'Chitake Soba'],
    "economy": ['Industrial manufacturing', 'Agriculture'],
    "name-kanji": "栃木県",
    "capital-kanji": "宇都宮市",
    "iso-code": "JP-09",
    "area-code": "028"
}

gunma = {
    "name": "Gunma",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Maebashi",
    "population": f"{gunma_population}",
    "density": f"{gunma_density}",
    "density-mi": f"{gunma_density_mi}",
    "area": "6,362.28 km2",
    "area-mi": "2,456.49 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Yaki Manjuu', 'Okkirikomi', 'Kamameshi'],
    "economy": ['Electrical equipment', 'Transport industry', 'Agriculture', 'Sericulture'],
    "name-kanji": "群馬県",
    "capital-kanji": "前橋市",
    "iso-code": "JP-10",
    "area-code": "027"
}

saitama = {
    "name": "Saitama",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Saitama",
    "population": f"{saitama_population}",
    "density": f"{saitama_density}",
    "density-mi": f"{saitama_density_mi}",
    "area": "3,797.75 km2",
    "area-mi": "1,466.32 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Hiyajiru Udon', 'Igamanjuu', 'Niboutou'],
    "economy": ['Car industry', 'Agriculture'],
    "name-kanji": "埼玉県",
    "capital-kanji": "さいたま市",
    "iso-code": "JP-11",
    "area-code": "048"
}

chiba = {
    "name": "Chiba",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Chiba",
    "population": f"{chiba_population}",
    "density": f"{chiba_density}",
    "density-mi": f"{chiba_density_mi}",
    "area": "5,157.61 km2",
    "area-mi": "1,991.36 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Namerou', 'Yude Rakkasei', 'Aji no Tataki'],
    "economy": ['Brewing industry', 'Chemical industry', 'Machine industry', 'Agriculture', 'Oil', 'Steel'],
    "name-kanji": "千葉県",
    "capital-kanji": "千葉市",
    "iso-code": "JP-12",
    "area-code": "043"
}

tokyo = {
    "name": "Tōkyō",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Shinjuku",
    "population": f"{tokyo_population}",
    "density": f"{tokyo_density}",
    "density-mi": f"{tokyo_density_mi}",
    "area": "2,194.07 km2",
    "area-mi": "847.14 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Monja Yaki', 'Fukagawa Don', 'Kusaya'],
    "economy": ['Finance', 'Light industry'],
    "name-kanji": "東京都",
    "capital-kanji": "新宿区",
    "iso-code": "JP-13",
    "area-code": "03x042"
}

kanagawa = {
    "name": "Kanagawa",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Yokohama",
    "population": f"{kanagawa_population}",
    "density": f"{kanagawa_density}",
    "density-mi": f"{kanagawa_density_mi}",
    "area": "2,415.83 km2",
    "area-mi": "932.76 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kaigun Kare', 'Namashirasu Don', 'Sanmamen'],
    "economy": ['Chemistry', 'Metallurgical industry', 'Transport industry', 'Electrical industry', 'Food industry'],
    "name-kanji": "神奈川県",
    "capital-kanji": "横浜市",
    "iso-code": "JP-14",
    "area-code": "045"
}

niigata = {
    "name": "Niigata",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Niigata",
    "population": f"{niigata_population}",
    "density": f"{niigata_density}",
    "density-mi": f"{niigata_density_mi}",
    "area": "12,584.18 km2",
    "area-mi": "4,858.78 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Noppei Jiru', 'SasaDango', 'Hegi Soba'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Mining', 'Manufacturing'],
    "name-kanji": "新潟県",
    "capital-kanji": "新潟市",
    "iso-code": "JP-15",
    "area-code": "25",
}

toyama = {
    "name": "Toyama",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Toyama",
    "population": f"{toyama_population}",
    "density": f"{toyama_density}",
    "density-mi": f"{toyama_density_mi}",
    "area": "4,247.61 km2",
    "area-mi": "1,640.01 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Masuzushi', 'Shiro Ebi Ryori', 'Hotaru Ika Ryori'],
    "economy": ['Agriculture', 'Manufacturing', 'Energy'],
    "name-kanji": "富山県",
    "capital-kanji": "富山市",
    "iso-code": "JP-16",
    "area-code": "076"
}

ishikawa = {
    "name": "Ishikawa",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Kanazawa",
    "population": f"{ishikawa_population}",
    "density": f"{ishikawa_density}",
    "density-mi": f"{ishikawa_density_mi}",
    "area": "4,186.09 km2",
    "area-mi": "1,616.26 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kabura Zushi', 'Jibuni', 'Kaga Ryori'],
    "economy": ['Textile industry', 'Artificial fabrics', 'Machine industry'],
    "name-kanji": "石川県",
    "capital-kanji": "金沢市",
    "iso-code": "JP-17",
    "area-code": "076"
}

fukui = {
    "name": "Fukui",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Fukui",
    "population": f"{fukui_population}",
    "density": f"{fukui_density}",
    "density-mi": f"{fukui_density_mi}",
    "area": "4,190.49 km2",
    "area-mi": "1,617.96 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Oroshi Soba', 'Satoimo no Koroni', 'Saba no Heshiko'],
    "economy": ['Nuclear power', 'Glasses production '],
    "name-kanji": "福井県",
    "capital-kanji": "福井市",
    "iso-code": "JP-18",
    "area-code": "077"
}

yamanashi = {
    "name": "Yamanashi",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Kōfu",
    "population": f"{yamanashi_population}",
    "density": f"{yamanashi_density}",
    "density-mi": f"{yamanashi_density_mi}",
    "area": "4,465.27 km2",
    "area-mi": "1,724.05 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Houtou', 'Yoshida no Udon', 'Kabocha Houtou'],
    "economy": ['Jewerly', 'Robotics', 'Wine production', 'Mineral water', 'Fruit growing'],
    "name-kanji": "山梨県",
    "capital-kanji": "甲府市",
    "iso-code": "JP-19",
    "area-code": "055"
}

nagano = {
    "name": "Nagano",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Nagano",
    "population": f"{nagano_population}",
    "density": f"{nagano_density}",
    "density-mi": f"{nagano_density_mi}",
    "area": "13,561.56 km2",
    "area-mi": "5,236.15 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Shinshuu Soba', 'Nozawanazuke', 'Oyaki'],
    "economy": ['Electronics', 'Information technology', 'Precision machinery', 'Agriculture', 'Tourism'],
    "name-kanji": "長野県",
    "capital-kanji": "長野市",
    "iso-code": "JP-20",
    "area-code": "026"
}

gifu = {
    "name": "Gifu",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Gifu",
    "population": f"{gifu_population}",
    "density": f"{gifu_density}",
    "density-mi": f"{gifu_density_mi}",
    "area": "10,621.29 km2",
    "area-mi": "4,100.90 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kurikinton', 'Keichan', 'Hobamiso'],
    "economy": ['Fishery', 'Heavy industry', 'Science', 'Paper', 'Tourism'],
    "name-kanji": "岐阜県",
    "capital-kanji": "岐阜市",
    "iso-code": "JP-21",
    "area-code": "058"
}

shizuoka = {
    "name": "Shizuoka",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Shizuoka",
    "population": f"{shizuoka_population}",
    "density": f"{shizuoka_density}",
    "density-mi": f"{shizuoka_density_mi}",
    "area": "7,777.42 km2",
    "area-mi": "3,002.88 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Sakuraebi Ryouri', 'Unagi No Kabayaki', 'Shizuoka Oden'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Tourism'],
    "name-kanji": "静岡県",
    "capital-kanji": "静岡市",
    "iso-code": "JP-22",
    "area-code": "054"
}

aichi = {
    "name": "Aichi",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Nagoya",
    "population": f"{aichi_population}",
    "density": f"{aichi_density}",
    "density-mi": f"{aichi_density_mi}",
    "area": "5,172.92 km2",
    "area-mi": "1,997.28 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Hitsumabushi', 'Miso Nikomi Udon', 'Tebasaki Karaage'],
    "economy": ['Heavy industry', 'Electronics', 'Transport industry'],
    "name-kanji": "愛知県",
    "capital-kanji": "名古屋市",
    "iso-code": "JP-23",
    "area-code": "052"
}

mie = {
    "name": "Mie",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Tsu",
    "population": f"{mie_population}",
    "density": f"{mie_density}",
    "density-mi": f"{mie_density_mi}",
    "area": "5,774.41 km2",
    "area-mi": "2,229.51 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Ise Udon', 'Tekonezushi', 'Ise Ebi Ryouri'],
    "economy": ['Handicraft', 'Forestry', 'Fishery', 'Agriculture', 'Manufacturing'],
    "name-kanji": "三重県",
    "capital-kanji": "津市",
    "iso-code": "JP-24",
    "area-code": "059"
}

shiga = {
    "name": "Shiga",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Ōtsu",
    "population": f"{shiga_population}",
    "density": f"{shiga_density}",
    "density-mi": f"{shiga_density_mi}",
    "area": "4,017.38 km2",
    "area-mi": "1,551.12 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Funazushi', 'Kamo Nabe', 'Ayu No Tsukudani'],
    "economy": ['Agriculture', 'Electronics', 'Manufacturing', 'Textile industry', 'Fishery'],
    "name-kanji": "滋賀県",
    "capital-kanji": "大津市",
    "iso-code": "JP-25",
    "area-code": "077"
}

kyoto = {
    "name": "Kyōto",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Kyōto",
    "population": f"{kyoto_population}",
    "density": f"{kyoto_density}",
    "density-mi": f"{kyoto_density_mi}",
    "area": "4,612.19 km2",
    "area-mi": "1,780.78 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kaiseki Ryori', 'Kyou Tsukemono', 'Obanzai'],
    "economy": ['Agriculture', 'Tourism', 'Forestry', 'Farming', 'Manufacturing'],
    "name-kanji": "京都府",
    "capital-kanji": "京都市",
    "iso-code": "JP-26",
    "area-code": "074"
}

osaka = {
    "name": "Ōsaka",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Ōsaka",
    "population": f"{osaka_population}",
    "density": f"{osaka_density}",
    "density-mi": f"{osaka_density_mi}",
    "area": "1,905.14 km2",
    "area-mi": "735.58 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Takoyaki', 'Okonomiyaki', 'Kitsune Udon'],
    "economy": ['Commercial sales', 'Electronics', 'Chemistry', 'Pharmaceutical', 'Heavy industry'],
    "name-kanji": "大阪府",
    "capital-kanji": "大阪市",
    "iso-code": "JP-27",
    "area-code": "06x"
}

hyogo = {
    "name": "Hyōgo",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Kōbe",
    "population": f"{hyogo_population}",
    "density": f"{hyogo_density}",
    "density-mi": f"{hyogo_density_mi}",
    "area": "8,400.94 km2",
    "area-mi": "3,243.62 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Akashiyaki', 'Kobe Beef', 'Ikanago no kukini'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Heavy & Metal industry', 'Medical industry', 'IT industry', 'Sea ports'],
    "name-kanji": "兵庫県",
    "capital-kanji": "神戸市",
    "iso-code": "JP-28",
    "area-code": "073"
}

nara = {
    "name": "Nara",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Nara",
    "population": f"{nara_population}",
    "density": f"{nara_density}",
    "density-mi": f"{nara_density_mi}",
    "area": "3,691.09 km2",
    "area-mi": "1,425.14 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kaki no Ha Zushi', 'Miwa Soumen', 'Yamato no Chagayu'],
    "economy": ['Agriculture', 'Tourism', 'Archeology', 'Traditional instruments', 'Aquaculture'],
    "name-kanji": "奈良県",
    "capital-kanji": "奈良市",
    "iso-code": "JP-29",
    "area-code": "074"
}

wakayama = {
    "name": "Wakayama",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Wakayama",
    "population": f"{wakayama_population}",
    "density": f"{wakayama_density}",
    "density-mi": f"{wakayama_density_mi}",
    "area": "4,724.69 km2",
    "area-mi": "1,824.21 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Kujira no Tatsuta Age', 'Meharizushi', 'Kue Nabe'],
    "economy": ['Agriculture', 'Tourism', 'Farming'],
    "name-kanji": "和歌山県",
    "capital-kanji": "和歌山市",
    "iso-code": "JP-30",
    "area-code": "075"
}

tottori = {
    "name": "Tottori",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Tottori",
    "population": f"{tottori_population}",
    "density": f"{tottori_density}",
    "density-mi": f"{tottori_density_mi}",
    "area": "3,507.05 km2",
    "area-mi": "1,354.08 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Matsubagani Ryouri', 'Kanijuu', 'Oyama Okowa'],
    "economy": ['Agriculture', 'Farming', 'Fishing', 'Seafood'],
    "name-kanji": "鳥取県",
    "capital-kanji": "鳥取市",
    "iso-code": "JP-31",
    "area-code": "085"
}

shimane = {
    "name": "Shimane",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Matsue",
    "population": f"{shimane_population}",
    "density": f"{shimane_density}",
    "density-mi": f"{shimane_density_mi}",
    "area": "6,708.24 km2",
    "area-mi": "2,590.07 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Izumo Soba', 'Shijimi Jiru', 'Taimeishi'],
    "economy": ['Retail industry', 'Manufacturing industry', 'Finance'],
    "name-kanji": "島根県",
    "capital-kanji": "松江市",
    "iso-code": "JP-32",
    "area-code": "085"
}

okayama = {
    "name": "Okayama",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Okayama",
    "population": f"{okayama_population}",
    "density": f"{okayama_density}",
    "density-mi": f"{okayama_density_mi}",
    "area": "7,114.50 km2",
    "area-mi": "2,746.92 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Okayama Barazushi', 'Hiruzen Okowa', 'Mamakari Zushi'],
    "economy": ['Tourism', 'Automotive manufacturing', 'Agricultural machinery', 'Shipbuilding'],
    "name-kanji": "岡山県",
    "capital-kanji": "岡山市",
    "iso-code": "JP-33",
    "area-code": "086"
}

hiroshima = {
    "name": "Hiroshima",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Hiroshima",
    "population": f"{hiroshima_population}",
    "density": f"{hiroshima_density}",
    "density-mi": f"{hiroshima_density_mi}",
    "area": "8,479.63 km2",
    "area-mi": "3,274.00 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Hiroshima Okonomiyaki', 'Kaki Ryouri', 'Anago Meshidon'],
    "economy": ['Tourism', 'Automobiles', 'Manufacturing'],
    "name-kanji": "広島県",
    "capital-kanji": "広島市",
    "iso-code": "JP-34",
    "area-code": "082"
}

yamaguchi = {
    "name": "Yamaguchi",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Yamaguchi",
    "population": f"{yamaguchi_population}",
    "density": f"{yamaguchi_density}",
    "density-mi": f"{yamaguchi_density_mi}",
    "area": "6,112.30 km2",
    "area-mi": "2,359.97 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Fugu Ryouri', 'Fugu Sashi', 'Shirouo Ryouri'],
    "economy": ['Machine building', 'Metallurgy', 'Textile', 'Chemical products'],
    "name-kanji": "山口県",
    "capital-kanji": "山口市",
    "iso-code": "JP-35",
    "area-code": "083"
}

tokushima = {
    "name": "Tokushima",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Tokushima",
    "population": f"{tokushima_population}",
    "density": f"{tokushima_density}",
    "density-mi": f"{tokushima_density_mi}",
    "area": "4,146.80 km2",
    "area-mi": "1,601.09 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Sobagome Zosui', 'Tarai Udon', 'Iya Soba'],
    "economy": ['Agriculture', 'Forestry', 'Fishery'],
    "name-kanji": "徳島県",
    "capital-kanji": "徳島市",
    "iso-code": "JP-36",
    "area-code": "088"
}

kagawa = {
    "name": "Kagawa",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Takamatsu",
    "population": f"{kagawa_population}",
    "density": f"{kagawa_density}",
    "density-mi": f"{kagawa_density_mi}",
    "area": "1,876.77 km2",
    "area-mi": "724.62 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Sanuki Udon', 'Shippoku Udon', 'Iriko Meshi'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Manufacturing'],
    "name-kanji": "香川県",
    "capital-kanji": "高松市",
    "iso-code": "JP-37",
    "area-code": "087"
}

ehime = {
    "name": "Ehime",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Matsuyama",
    "population": f"{ehime_population}",
    "density": f"{ehime_density}",
    "density-mi": f"{ehime_density_mi}",
    "area": "5,676.23 km2",
    "area-mi": "2,191.60 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Uwajima Tai Meshi', 'Jakoten', 'Satsuma-jiru'],
    "economy": ['Agriculture', 'Fishery', 'Ship building', 'Chemical industry', 'Electric power'],
    "name-kanji": "愛媛県",
    "capital-kanji": "松山市",
    "iso-code": "JP-38",
    "area-code": "089"
}

kochi = {
    "name": "Kōchi",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Kōchi",
    "population": f"{kochi_population}",
    "density": f"{kochi_density}",
    "density-mi": f"{kochi_density_mi}",
    "area": "7,103.93 km2",
    "area-mi": "2,742.84 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Katsuo no Tataki', 'Sawachi Ryouri', 'Katsuo no Tosazukuri'],
    "economy": ['Oil refining', 'Spices and seafood', 'Ship building', 'Chemical industry', 'Retail', 'Electronics hardware'],
    "name-kanji": "高知県",
    "capital-kanji": "高知市",
    "iso-code": "JP-39",
    "area-code": "088"
}

fukuoka = {
    "name": "Fukuoka",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Fukuoka",
    "population": f"{fukuoka_population}",
    "density": f"{fukuoka_density}",
    "density-mi": f"{fukuoka_density_mi}",
    "area": "4,986.52 km2",
    "area-mi": "1,925.31 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Mentaiko', 'Motsu Nabe', 'Tori no Mizutaki'],
    "economy": ['Automobiles', 'Electronics', 'Steel'],
    "name-kanji": "福岡県",
    "capital-kanji": "福岡市",
    "iso-code": "JP-40",
    "area-code": "082"
}

saga = {
    "name": "Saga",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Saga",
    "population": f"{saga_population}",
    "density": f"{saga_density}",
    "density-mi": f"{saga_density_mi}",
    "area": "2,440.68 km2",
    "area-mi": "942.35 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Yobiko no Ika Ryouri', 'Mutsugurou no Kabayaki', 'Dagojiru'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name-kanji": "佐賀県",
    "capital-kanji": "佐賀市",
    "iso-code": "JP-41",
    "area-code": "095"
}

nagasaki = {
    "name": "Nagasaki",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Nagasaki",
    "population": f"{nagasaki_population}",
    "density": f"{nagasaki_density}",
    "density-mi": f"{nagasaki_density_mi}",
    "area": "4,130.88 km2",
    "area-mi": "1,594.94 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Sara Udon / Chanpon', 'Shippoku Ryori', 'Sasebo Burger'],
    "economy": ['Heavy industry', 'Agriculture'],
    "name-kanji": "長崎県",
    "capital-kanji": "長崎市",
    "iso-code": "JP-42",
    "area-code": "095"
}

kumamoto = {
    "name": "Kumamoto",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Kumamoto",
    "population": f"{kumamoto_population}",
    "density": f"{kumamoto_density}",
    "density-mi": f"{kumamoto_density_mi}",
    "area": "7,409.48 km2",
    "area-mi": "2,860.82 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Basashi', 'Ikinari Dango', 'Karashirenkon'],
    "economy": ['Tourism', 'Automobiles'],
    "name-kanji": "熊本県",
    "capital-kanji": "熊本市",
    "iso-code": "JP-43",
    "area-code": "096"
}

oita = {
    "name": "Ōita",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Ōita",
    "population": f"{oita_population}",
    "density": f"{oita_density}",
    "density-mi": f"{oita_density_mi}",
    "area": "6,340.73 km2",
    "area-mi": "2,448.17 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Buri no Atsumeshi', 'Gomadashi Udon', 'Tenobe Dango Jiru'],
    "economy": ['Tourism', 'Agriculture', 'Seafood', 'Forestry'],
    "name-kanji": "大分県",
    "capital-kanji": "大分市",
    "iso-code": "JP-44",
    "area-code": "097"
}

miyazaki = {
    "name": "Miyazaki",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Miyazaki",
    "population": f"{miyazaki_population}",
    "density": f"{miyazaki_density}",
    "density-mi": f"{miyazaki_density_mi}",
    "area": "7,735.32 km2",
    "area-mi": "2,986.62 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Miyazaki no Sumibiyaki', 'Hiyajiru', 'Chicken Nanban'],
    "economy": ['Forestry', 'Agriculture', 'Fishery', 'Forestry', 'Textile', 'Electronics'],
    "name-kanji": "宮崎県",
    "capital-kanji": "宮崎市",
    "iso-code": "JP-45",
    "area-code": "098"
}

kagoshima = {
    "name": "Kagoshima",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Kagoshima",
    "population": f"{kagoshima_population}",
    "density": f"{kagoshima_density}",
    "density-mi": f"{kagoshima_density_mi}",
    "area": "9,187.01 km2",
    "area-mi": "3,547.12 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Tori Meshi', 'Kibinago Ryouri', 'Tonkotsu Ryouri'],
    "economy": ['Agriculture', 'Ceramic industry', 'Electronics'],
    "name-kanji": "鹿児島県",
    "capital-kanji": "鹿児島市",
    "iso-code": "JP-46",
    "area-code": "099"
}

okinawa = {
    "name": "Okinawa",
    "region": "Kyushu",
    "island": "Ryukyu Islands",
    "capital": "Naha",
    "population": f"{okinawa_population}",
    "density": f"{okinawa_density}",
    "density-mi": f"{okinawa_density_mi}",
    "area": "2,280.98 km2",
    "area-mi": "880.69 sq mi",
    "climate": "Humid subtropical",
    "local-dishes": ['Soki Soba', 'Goya Chanpuru', 'Rafutee'],
    "economy": ['Military', 'Tourism', 'Agriculture', 'Fishery', 'Retail', 'Civil engineering', 'Petroleum'],
    "name-kanji": "沖縄県",
    "capital-kanji": "那覇市",
    "iso-code": "JP-47",
    "area-code": "098"
}
