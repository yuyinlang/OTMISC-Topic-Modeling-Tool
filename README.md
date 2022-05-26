# Topic modeling advancements

**Supervisor:** Professor Dr. Georg Groh

**Advisors:** PhD Candidate (M.Sc.) Miriam Anschütz, PhD Candidate (M.Sc.) Ahmed Mosharafa

**Project Scope:**

* Evaluating different Topic Modeling algorithms on short/long text dataset
* Drawing observations on the applicability of certain algorithms’ clusters to different types of datasets.
* Having an outcome including metric-based evaluation, as well as, human based evaluation to the algorithms.


## Milestone #01: Datasets and Data Exploration

* Explored the provided datasets to unveil the inherent characteristics.
* Obtained an overview of the statistical characteristics of the datasets.
* **Included Datasets:**
  * CRISIS NLP: https://crisisnlp.qcri.org/.
  * 20NewsGroups: http://qwone.com/~jason/20Newsgroups/.

### Overview of All Dataset Resources

| Resource Name             | Is Suitable? | Type                                | Contains Tweet Text? | Event Count | Event Distribution                                                                                                                                                                                                                                                                                                        |
|---------------------------|--------------|-------------------------------------|----------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRISIS NLP - Resource #01 | Yes          | Short Text Dataset                  | Yes                  | 12          | (2K - 2K - 2K - 2K - 2K - 1K - 2K - 1K - 2K - 2K - 2K - 3K)                                                                                                                                                                                                                                                               |
| CRISIS NLP - Resource #02 | Yes          | Short Text Dataset                  | Yes                  | 7           | (1K - 1K - 2K - 1K - 1K - 13K - 5K)                                                                                                                                                                                                                                                                                       |
| CRISIS NLP - Resource #03 | Yes          | Short Text Dataset                  | Yes                  | 6           | (2K - 1K - 9K - 1K - 2K - 2K)                                                                                                                                                                                                                                                                                             |
| CRISIS NLP - Resource #04 | No           | A Tool for LSTM RNNs                | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #05 | Yes          | Short Text Dataset                  | Yes                  | 7           | (1K - 4K - 4K - 4K - 0.5K - 1K - 1K)                                                                                                                                                                                                                                                                                      |
| CRISIS NLP - Resource #06 | Yes          | Short Text Dataset                  | No                   | 3           | (1207K - 1096K - 6506K)                                                                                                                                                                                                                                                                                                   |
| CRISIS NLP - Resource #07 | Yes          | Short Text Dataset                  | Yes                  | 2           | (12K - 10K)                                                                                                                                                                                                                                                                                                               |
| CRISIS NLP - Resource #08 | No           | A Tool for Tweets Retrieval Tool    | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #09 | No           | Image Dataset                       | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #10 | Yes          | Short Text Dataset                  | Yes                  | 2           | (12K - 10K)                                                                                                                                                                                                                                                                                                               |
| CRISIS NLP - Resource #11 | No           | Text Dataset with Name Lists        | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #12 | Yes          | Short Text Dataset for Eye Witness  | Yes                  | 4           | (2K - 2K - 2K - 2K)                                                                                                                                                                                                                                                                                                       |
| CRISIS NLP - Resource #13 | No           | Image Dataset                       | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #14 | No           | Geo-Location Data                   | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #15 | No           | Image Dataset                       | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |
| CRISIS NLP - Resource #16 | Yes          | Short Text Dataset                  | Yes                  | 61          | (2K - 3K - 2K - 2K - 2K - 2K - 2K - 2K - 20K - 1K - 1K - 2K - 2K - 20K - 2K - 2K - 2K - 2K - 20K - 2K - 2K - 2K - 2K - 2K - 2K - 2K - 2K - 20K - 4K - 2K - 2K - 20K - 2K - 2K - 2K - 2K - 20K - 9K - 4K - 5K - 6K - 1K - 3K - 0K - 4K - 4K - 4K - 4K - 19K - 4K - 25K - 4K - 1K - 3K - 53K - 8K - 8K - 8K - 1K - 2K - 2K) |
| CRISIS NLP - Resource #17 | Yes          | Short Text Dataset                  | Yes                  | 17          | (7K - 2K - 4K - 2K - 8K - 6K - 9K - 9K - 7K - 2K - 1K - 2K - 8K - 2K - 2K - 2K - 1K)                                                                                                                                                                                                                                      |
| CRISIS NLP - Resource #18 | No           | Text Dataset for Sentiment Analysis | -                    | -           | -                                                                                                                                                                                                                                                                                                                         |


## Deployment and Run

### Build

* For Linux, It is enough to run the following command for setting up virtual environment and install dependencies.

```bash
$ ./build_for_linux.sh
```

* For windows and other operating systems, install `python 3.8`, and install dependencies
  with `pip install -r requirements.txt`. Be careful about the package versions and make sure that you have the correct
  version in your current set up!

### Run

To run the Jupyter Notebook, just execute the following command:

```bash
$ ./run_jupyter.sh
```

* For windows and other operating systems, it can be done via Anaconda or similar tools.

## References
* Csv to Markdown Table Converter #1: https://tableconvert.com/.
* Csv to Markdown Table Converter #2: https://markdown.co/tool/csv-to-markdown-table.
* Angelov: Top2vec: Distributed representations of topics
* Grootendorst: BERTopic (https://github.com/MaartenGr/BERTopic)
