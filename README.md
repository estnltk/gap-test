# Gap Test Benchmark


In a gap filling test, the goal is to fill a fixed missing word in a sentence with a right word from a list of suggested candidates.
Given a sentence with a gap and a list of candidates, the system should score each candidate and report the rank of the original word.
To make the task more challenging, we created multiple versions of the test, taking into account word frequencies and a way the candidates are generated.
This benchmark suite provides the necessary data and tools to assess system performance in the gap filling test.

## Data
The benchmark dataset originates from the Estonian Reference Corpus [1], which consists of 16M sentences, 55M words and 3M types.
The corpus pre-processing, including sentence and word tokenization, has been performed using the estnltk toolkit [2].

## Sentence file
From the pre-processed corpus we sampled 7K random sentences of 4-16 words.
In each sentence we then marked one random word as a gap.

Based on the frequency of a gap-word, we generated four versions of test sets, so that each test set contains only gap-words falling into a certain frequency range.
We define the following frequency groups:

1. all words of any frequency
2. frequent words (frequency 0.00001-0.0001)
3. words with an infrequent (frequency less than 0.00001) inflectional form and a frequent base form
4. words with an infrequent inflectional form and an infrequent base form.

A test file contains one sentence per line.
The words in a sentence are lowercased and space delimited.
Each line starts with a number which denotes a zero-based word-offset of a gap word in the sentence (the gap word itself is not removed from the sentence).

## Candidate file
Each sentence file is accompanied with a number of candidate files.
A candidate file lists 200 candidate words for each test sentence.
We provide candidate sets generated using three different approaches.
In the first case, candidates are randomly sampled from the whole vocabulary.
In the second case, candidates are randomly sampled from the set of words with the same part of speech tag as the gap-word.
The third candidate set is based on word2vec word embeddings.
It contains top 200 words with the closest vector to the gap-word measured by cosine similarity.

Similarly to a gap test, we created four samples of candidates of a different frequency.
We used the same frequency ranges as in a case of a gap test. As a result, there are 12 (3 types X 4 frequency groups) candidate files per test file.

## Running the test
To run a gap test, one requires a pair of a test and a candidate file.
For each sentence in the test file, the program should score the corresponding candidates and output the rank of the original gap word.
See a script *example_test.py* for example.

To measure the accuracy, we provide a script *eval.py*.
It reads in the rankings produced by the first script and reports the accuracy at levels 1 to 10.
The following example demonstrates how to run test and evaluation scripts:

```bash
$ python example_test.py “gap test file” “candidate file” > python eval.py
$ 0.4,0.6,0.9,1.0,1.0,1.0,1.0,1.0,1.0,1.0
```

## Data files
The benchmark dataset consists of the gap test files with an extension *.gap*, and the variant files with an extension *.var*.
The dataset can be downloaded from http://ats.cs.ut.ee/keeletehnoloogia/estnltk/gap-test-benchmark.tar.gz

## References
1. Estonian Reference Corpus http://www.cl.ut.ee/korpused/segakorpus/
2. Estnltk -- Open source tools for Estonian natural language processing http://github.com/estnltk/estnltk


