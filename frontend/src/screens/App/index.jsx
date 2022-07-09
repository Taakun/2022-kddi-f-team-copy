/* eslint-disable */

import { Component } from 'react';

import getQuestion from '../../utils/getQuestion';
import TutorialModal from '../../components/TutorialModal';

import './styles.css';

const numberOfQuestions = 13;

function SearchContainer({ question, answersButtons, onButtonClick }) {
  return (
    <div className="searchContainer">
      <div className="pr-10 pb-20">
        <img src="/brain.png" alt="" />
      </div>
      <h2>{question}</h2>
      <div>
        {answersButtons.map((answer) => (
          <button key={Math.random()} onClick={() => onButtonClick(answer.value)}>
            {answer.title}
          </button>
        ))}
      </div>
    </div>
  );
}

class App extends Component {
  state = {
    alreadyFeatures: [],
    params: [],
    answers: [],
    answersButtons: [],
    question: '',
    characterMatch: null,
    loading: true,
    finished: false,
  };

  componentWillMount() {
    this.setQuestion();
  }

  setQuestion = async () => {
    this.setState({ loading: true });

    try {
      const { alreadyFeatures, params } = this.state;
      const { answers, characterMatch, feature, param, question } = await getQuestion(
        alreadyFeatures,
        params,
        this.state.answers,
      );
      this.setState({
        params: [...this.state.params, param],
        alreadyFeatures: [...this.state.alreadyFeatures, feature],
        answersButtons: answers,
        characterMatch,
        question,
        loading: false,
        finished: this.state.finished || !question,
      });
    } catch (error) {
      console.log(error);
      this.setState({ loading: false });
      alert('Error on get Question');
    }
  };

  onButtonClick = async (answer) => {
    await this.setState({ answers: [...this.state.answers, answer] });
    await this.setQuestion();

    const finished = this.state.answers.length === numberOfQuestions;

    if (finished) this.setState({ finished: true });
  };

  onRetryButtonClick = async () => {
    try {
      this.setState({
        alreadyFeatures: [],
        params: [],
        answers: [],
        answersButtons: [],
        question: '',
        characterMatch: null,
        loading: true,
        finished: false,
      });
      const { answers, characterMatch, feature, param, question } = await getQuestion([], [], []);
      this.setState({
        params: [...this.state.params, param],
        alreadyFeatures: [...this.state.alreadyFeatures, feature],
        answersButtons: answers,
        characterMatch,
        question,
        loading: false,
        finished: this.state.finished || !question,
      });
    } catch (error) {
      console.log(error);
      this.setState({ loading: false });
      alert('Error on get Question');
    }
  };

  render() {
    const { question, answersButtons, loading, finished, characterMatch } = this.state;

    return (
      <div className="app">
        <header>
          <h1 className="text-5xl sans-serif">ナツネーター</h1>
          <h2 className="text-xl text-pink-700">〜僕と魔神の夏休み〜</h2>
        </header>
        <TutorialModal />
        <main>
          {loading && !finished ? <h2>Carregando..</h2> : null}
          {!loading && !finished ? (
            <SearchContainer question={question} answersButtons={answersButtons} onButtonClick={this.onButtonClick} />
          ) : null}
          {finished ? (
            <div className="finishedContainer">
              <img src={characterMatch.image} alt="" />
              <h2>{characterMatch.name}</h2>
              <button className="mt-20" onClick={this.onRetryButtonClick}>
                最初からやり直す
              </button>
            </div>
          ) : null}
        </main>
      </div>
    );
  }
}

export default App;
