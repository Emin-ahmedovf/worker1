import random
kelimeler = ["gözel","məlumat","xəta","sağalmaq","buraxmaq","vaxt","su","etmək","işlətmək","deyil","görmek",
             "çoxdan", "çoxu", "yaxşı", "pul", "oynamaq", "gül", "şəhər", "yüksəltmək", "emin", "varlıq", "etmək",
             "güvən", "gərək", "müalicə", "bilik", "rahat", "soyuq", "onsuz", "kitap", "paylaşmaq", "hesab", "bədən",
             "torpaq", "bənzər", "sistem", "xoş", "çəkilmək", "texnik", "yaxinlaşmaq", "ilik", "tarix", "kəsin", "bacı",
             "incə", "əyər", "onsuz", "qarşılıq","vermek", "sahip", "artıq", "kişi", "digər", "sonra", "yene", "hamsı",
             "kitap", "sevgi", "baxmaq", "sən", "dövlət", "qabaq", "son", "baxmaq", "üstündə", "belə", "bəzi", "mağaza",
             "tutmaq", "birbir", "heçnə", "yol", "su", "hava", "hal", "doğru", "orta", "başqa", "böyük", "eləmək",
             "yeni", "çoxlu", "soruşmaq", "onlar", "açmaq", "həm", "dərman", "səs", "həyat", "deyil", "saat", "yaraşıqlı", "necə",
             'bağlanmaq',"çekmek","atmaq","vurmaq","idman","bot","top","almaz","kral","kraliça","arı","saat","maaş","çörek","it","bitki","gecə","ev",
             "çöl","gec","tez","alim","ağıl","bilik","zəka","yastıq","yorqan","hörümçək","tibb","polis","odun","boy","qisas","söz"
             ]


def kelime_sec():
    return random.choice(kelimeler)
