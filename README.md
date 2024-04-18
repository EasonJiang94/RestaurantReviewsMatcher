# Env
You must follow the instruction of the Stanford CoreNLP to install the package

https://stanfordnlp.github.io/CoreNLP/download.html

If you haven't installed java, please install that first. It's nessesary. 

https://www.java.com/en/download/

## Issues I met
If you encounter the error when you install the python lib `gensim` : 
```text=1
ImportError: cannot import name 'triu' from 'scipy.linalg'
```
Please reinstall scipy with version 1.10.1
```bash=1
pip install scipy==1.10.1
```

# Usage
After you setup your env, run the CoreNLP server under the directory `stanford-corenlp-4.x.x`:
```bash=1
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```

Then you can run the test code:
```bash=1
cd src/
python3 Assignment4Main.py  
```

expected result : 
```txt=1
[co-worker, old] appears in review 	[ 1 ]
[meal, wonderful] appears in review 	[ 1 ]
[salad, huge] appears in review 	[ 1 ]
[stick, little] appears in review 	[ 1 ]
[stick, delicious] appears in review 	[ 1 ]
[service, excellent] appears in review 	[ 1 ,   2 ]
[this, place] appears in review 	[ 1 ]
[place, great] appears in review 	[ 1 ]
[experience, upscale] appears in review 	[ 1 ]
[spot, other] appears in review 	[ 1 ]
[restaurant, old] appears in review 	[ 2 ]
[woodwork, ornate] appears in review 	[ 2 ]
[tablecloth, white] appears in review 	[ 2 ]
[potato, red] appears in review 	[ 2 ]
[potato, skinned] appears in review 	[ 2 ]
[potato, mash] appears in review 	[ 2 ]
[meat, tender] appears in review 	[ 2 ]
[slaw, delicious] appears in review 	[ 2 ]
[I, picky] appears in review 	[ 2 ]
[atmosphere, nice] appears in review 	[ 3 ]
[list, local] appears in review 	[ 3 ]
[list, great] appears in review 	[ 3 ]
[taco, world] appears in review 	[ 3 ]
[sandwich, world] appears in review 	[ 3 ]
[potion, huge] appears in review 	[ 3 ]
[menu, huge] appears in review 	[ 3 ]
[that, thing] appears in review 	[ 3 ]
[thing, good] appears in review 	[ 3 ]
[person, regular] appears in review 	[ 3 ]
[note, positive] appears in review 	[ 4 ]
[meal, delicious] appears in review 	[ 4 ]
[sandwich, grill] appears in review 	[ 4 ]
[fries, amazing] appears in review 	[ 4 ]
[option, choose] appears in review 	[ 4 ]
[option, something] appears in review 	[ 4 ]
[ambiance, nice] appears in review 	[ 4 ]
[selection, great] appears in review 	[ 4 ]
[server, rude] appears in review 	[ 4 ]
[she, short] appears in review 	[ 4 ]
[we, young] appears in review 	[ 4 ]
[restaurant, small] appears in review 	[ 4 ,   5 ]
[table, one] appears in review 	[ 4 ]
[table, own] appears in review 	[ 4 ]
[ride, useless] appears in review 	[ 5 ]
[distance, walk] appears in review 	[ 5 ]
[it, meal] appears in review 	[ 5 ]
[meal, good] appears in review 	[ 5 ]
[I, fan] appears in review 	[ 5 ]
[fan, huge] appears in review 	[ 5 ]
[service, great] appears in review 	[ 5 ,   1 4 ]
[drink, large] appears in review 	[ 5 ]
[sandwich, French] appears in review 	[ 5 ]
[restaurant, nice] appears in review 	[ 5 ]
[atmosphere, great] appears in review 	[ 5 ]
[food, great] appears in review 	[ 5 ]
[place, rotation] appears in review 	[ 6 ]
[rotation, regular] appears in review 	[ 6 ]
[food, excellent] appears in review 	[ 6 ,   1 3 ]
[Devonshire, awesome] appears in review 	[ 6 ]
[desert, recent] appears in review 	[ 6 ]
[desert, mini] appears in review 	[ 6 ]
[bottle, deal] appears in review 	[ 6 ,   1 2 ]
[deal, great] appears in review 	[ 6 ]
[selection, good] appears in review 	[ 6 ]
[they, undercooked] appears in review 	[ 7 ]
[quality, bad] appears in review 	[ 7 ]
[it, day] appears in review 	[ 7 ]
[day, bad] appears in review 	[ 7 ]
[food, good] appears in review 	[ 8 ]
[food, hearty] appears in review 	[ 8 ]
[price, decent] appears in review 	[ 8 ]
[service, warm] appears in review 	[ 8 ]
[fish, battered] appears in review 	[ 8 ]
[trout, treat] appears in review 	[ 8 ]
[good, bad] appears in review 	[ 8 ]
[service, bad] appears in review 	[ 9 ]
[finger, homemade] appears in review 	[ 1 0 ]
[beer, good] appears in review 	[ 1 0 ]
[beer, price] appears in review 	[ 1 0 ]
[value, great] appears in review 	[ 1 0 ]
[menu, large] appears in review 	[ 1 1 ]
[portion, large] appears in review 	[ 1 1 ]
[price, reasonable] appears in review 	[ 1 1 ]
[quality, excellent] appears in review 	[ 1 1 ]
[menu, entire] appears in review 	[ 1 1 ]
[speciality, other] appears in review 	[ 1 1 ]
[speciality, cake] appears in review 	[ 1 1 ]
[restaurant, favorite] appears in review 	[ 1 2 ]
[favorite, top] appears in review 	[ 1 2 ]
[favorite, local] appears in review 	[ 1 2 ]
[feeling, warm] appears in review 	[ 1 2 ]
[deal, cheap] appears in review 	[ 1 2 ]
[portion, generous] appears in review 	[ 1 2 ]
[order, particular] appears in review 	[ 1 2 ]
[you, hungry] appears in review 	[ 1 2 ]
[course, main] appears in review 	[ 1 2 ]
[soup, French] appears in review 	[ 1 2 ]
[summer, last] appears in review 	[ 1 3 ]
[time, wonderful] appears in review 	[ 1 3 ]
[service, solid] appears in review 	[ 1 3 ]
[group, large] appears in review 	[ 1 3 ,   1 6 ]
[Grill, good] appears in review 	[ 1 4 ]
[turkey, roasted] appears in review 	[ 1 4 ]
[food, fresh] appears in review 	[ 1 4 ,   1 8 ]
[food, interesting] appears in review 	[ 1 4 ]
[taco, good] appears in review 	[ 1 5 ]
[it, big] appears in review 	[ 1 5 ]
[waiter, slow] appears in review 	[ 1 5 ]
[time, long] appears in review 	[ 1 5 ]
[thing, second] appears in review 	[ 1 5 ]
[thing, sure] appears in review 	[ 1 5 ]
[I, sure] appears in review 	[ 1 5 ]
[food, cold] appears in review 	[ 1 5 ]
[Drew, group] appears in review 	[ 1 6 ]
[food, satisfying] appears in review 	[ 1 6 ]
[food, typical] appears in review 	[ 1 6 ]
[food, American] appears in review 	[ 1 6 ]
[way, bad] appears in review 	[ 1 6 ]
[it, wonderful] appears in review 	[ 1 6 ]
[option, vegan] appears in review 	[ 1 6 ]
[salad, large] appears in review 	[ 1 7 ]
[salad, onion] appears in review 	[ 1 7 ]
[salad, Greek] appears in review 	[ 1 7 ]
[nacho, good] appears in review 	[ 1 7 ]
[fries, great] appears in review 	[ 1 7 ]
[waiter, friendly] appears in review 	[ 1 7 ]
[they, wine] appears in review 	[ 1 8 ]
[wine, decent] appears in review 	[ 1 8 ]
[noir, favorite] appears in review 	[ 1 8 ]
[food, fast] appears in review 	[ 1 8 ]
[restaurant, busy] appears in review 	[ 1 9 ]
[hope, high] appears in review 	[ 1 9 ]
[I, disappointed] appears in review 	[ 1 9 ]
[food, ok] appears in review 	[ 1 9 ]
[service, good] appears in review 	[ 2 0 ]
[ambience, pleasant] appears in review 	[ 2 0 ]
[pittsburgher, old] appears in review 	[ 2 0 ]
[service, awful] appears in review 	[ 2 1 ,   2 3 ]
[service, disaster] appears in review 	[ 2 2 ]

--------------------------------------------------------------

query opinion [service, good] has similar opinions: 
    [service, excellent] appears in review 	[ 1 ,   2 ]
    [service, great] appears in review 	[ 5 ,   1 4 ]
    [service, warm] appears in review 	[ 8 ]
    [service, solid] appears in review 	[ 1 3 ]
    [service, good] appears in review 	[ 2 0 ]

query opinion [service, bad] has similar opinions: 
    [service, bad] appears in review 	[ 9 ]

query opinion [atmosphere, good] has similar opinions: 
    [atmosphere, nice] appears in review 	[ 3 ]
    [ambiance, nice] appears in review 	[ 4 ]
    [atmosphere, great] appears in review 	[ 5 ]
    [feeling, warm] appears in review 	[ 1 2 ]
    [ambience, pleasant] appears in review 	[ 2 0 ]

query opinion [food, delicious] has similar opinions: 
    [meal, wonderful] appears in review 	[ 1 ]
    [salad, huge] appears in review 	[ 1 ]
    [meat, tender] appears in review 	[ 2 ]
    [taco, world] appears in review 	[ 3 ]
    [sandwich, world] appears in review 	[ 3 ]
    [menu, huge] appears in review 	[ 3 ]
    [meal, delicious] appears in review 	[ 4 ]
    [fries, amazing] appears in review 	[ 4 ]
    [restaurant, small] appears in review 	[ 4 ,   5 ]
    [meal, good] appears in review 	[ 5 ]
    [drink, large] appears in review 	[ 5 ]
    [restaurant, nice] appears in review 	[ 5 ]
    [food, great] appears in review 	[ 5 ]
    [food, excellent] appears in review 	[ 6 ,   1 3 ]
    [food, good] appears in review 	[ 8 ]
    [food, hearty] appears in review 	[ 8 ]
    [beer, good] appears in review 	[ 1 0 ]
    [beer, price] appears in review 	[ 1 0 ]
    [menu, large] appears in review 	[ 1 1 ]
    [menu, entire] appears in review 	[ 1 1 ]
    [restaurant, favorite] appears in review 	[ 1 2 ]
    [turkey, roasted] appears in review 	[ 1 4 ]
    [food, fresh] appears in review 	[ 1 4 ,   1 8 ]
    [food, interesting] appears in review 	[ 1 4 ]
    [taco, good] appears in review 	[ 1 5 ]
    [food, satisfying] appears in review 	[ 1 6 ]
    [food, typical] appears in review 	[ 1 6 ]
    [salad, large] appears in review 	[ 1 7 ]
    [fries, great] appears in review 	[ 1 7 ]
    [wine, decent] appears in review 	[ 1 8 ]
    [food, fast] appears in review 	[ 1 8 ]
    [restaurant, busy] appears in review 	[ 1 9 ]
    [food, ok] appears in review 	[ 1 9 ]

--------------------------------------------------------------

```

