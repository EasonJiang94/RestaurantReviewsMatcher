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
python3 Assignment4Main.py  
```

# Next Step
According to the test result of test_word2vec.py : 
```text=1
The similarity of 'good' and 'great' is 0.7291509509086609
The similarity of 'good' and 'bad' is 0.7190050482749939
The similarity of 'service' and 'waiter' is 0.1305151730775833
The similarity of 'service' and 'atmosphere' is 0.08113634586334229
The similarity of 'service' and 'feeling' is 0.019352521747350693
The similarity of 'service' and 'atmosphere' is 0.08113634586334229
The similarity of 'service' and 'ambience' is 0.17133253812789917
The similarity of 'food' and 'meal' is 0.543371319770813
The similarity of 'delicious' and 'interesting' is 0.31214892864227295
The similarity of 'delicious' and 'hearty' is 0.5545052289962769
The similarity of 'delicious' and 'fresh' is 0.33691078424453735
The similarity of 'good' and 'delicious' is 0.28821617364883423
The similarity of 'good' and 'hearty' is 0.32131192088127136
The similarity of 'good' and 'fresh' is 0.26192352175712585
The similarity of 'good' and 'interesting' is 0.4272798001766205
The similarity of 'bad' and 'delicious' is 0.15252012014389038
The similarity of 'bad' and 'hearty' is 0.18113990128040314
The similarity of 'bad' and 'fresh' is 0.21413351595401764
The similarity of 'bad' and 'interesting' is 0.27719444036483765
The similarity of 'positive' and 'delicious' is 0.11241991817951202
The similarity of 'positive' and 'hearty' is 0.14521853625774384
The similarity of 'positive' and 'fresh' is 0.26131775975227356
The similarity of 'positive' and 'interesting' is 0.32780200242996216
```
We can tell the positive/negative adjectives by their similarity with good/bad. 

However, tasks like determining "service is good" and "waiter is good" are the next issue. 

