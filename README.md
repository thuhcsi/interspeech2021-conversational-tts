> Link to the paper: [Spoken Style Learning with Multi-modal Hierarchical Context Encoding for Conversational Text-to-Speech Synthesis](https://github.com/thuhcsi/interspeech2021-conversational-tts/raw/master/IS2021.PDF)

## Samples of synthesized speech

### Sample 1

#### Historical Conversations Text

Chinese: 我的天啊这大小姐是真的费|我不看会儿行不|马上就能去吃东西了好开心|这猴子还好吧|等等我马上到

English Translation: ----------

#### Historical Conversations Speech

<audio controls>
  <source src="https://github.com/thuhcsi/interspeech2021-conversational-tts/raw/master/context/sample0.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

#### Synthesized speech

* Baseline approach
<audio controls>
  <source src="https://github.com/thuhcsi/interspeech2019-tts-samples/raw/master/sample1-baseline.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

* Proposed approach
<audio controls>
  <source src="https://github.com/thuhcsi/interspeech2019-tts-samples/raw/master/sample1-proposed.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

#### Explanation

The baseline approach has word tokenization error around the 3-rd character,
resulting in pause deletion between the 2-nd and the 3-rd characters and improper pause insertion between the 3-rd and 4-th characters,
changing the meaning to `Xu Wen Gen we share your answer`.

The baseline approach also has syllable pronunciation error at the 8-th character,
incorrectly predicting the pronunciation of the character from `yi2` to `yi4`.

The proposed system has synthesized the speech with expected pronunciations and pauses.

### Sample 2

#### Text

Chinese: 用科技推动教育进步是我们的理念。

English Translation: Using technology to push the evolution of education is our concept.

#### Synthesized speech

* Baseline approach
<audio controls>
  <source src="https://github.com/thuhcsi/interspeech2019-tts-samples/raw/master/sample2-baseline.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

* Proposed approach
<audio controls>
  <source src="https://github.com/thuhcsi/interspeech2019-tts-samples/raw/master/sample2-proposed.wav" type="audio/wav">
Your browser does not support the audio element.
</audio>

#### Explanation

The baseline system synthesized the speech with expected pronunciations.
However the baseline approach has pause deletion between the 7-nd and the 8-rd characters and improper pause insertion between the 9-rd and 10-th characters,
changing the meaning to `Using technology to push the education. Evolution is our concept`.

The proposed system has synthesized the speech with expected pronunciations and pauses.
