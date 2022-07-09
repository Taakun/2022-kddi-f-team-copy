import React, { Component } from 'react';

import getQuestion from '../../utils/getQuestion';
import TutorialModal from '../../components/TutorialModal';

import './styles.css';

const numberOfQuestions = 13;

const SearchContainer = ({ question, answersButtons, onButtonClick }) => (
  <div className="searchContainer">
    <img src="/brain.png" alt="" />
    <h2>{ question }</h2>
    <div>
      { answersButtons.map(answer => <button key={Math.random()} onClick={() => onButtonClick(answer.value)}>{ answer.title }</button>) }
    </div>
  </div>
);

const FinishedContainer = ({ characterMatch }) => (
  <div className="finishedContainer">
    <img src={characterMatch.image} alt="" />
    <h2>{ characterMatch.name }</h2>
  </div>
);

class App extends Component {
  state = {
    alreadyFeatures: [],
    params: [],
    answers: [],
    answersButtons: [],
    question: '',
    characterMatch: null,
    loading: true,
    finished: false
  };

  componentWillMount() {
    this.setQuestion();
  }

  setQuestion = async () => {
    this.setState({ loading: true });

    try {
      const { alreadyFeatures, params } = this.state;
      const { answers, characterMatch, feature, param, question } = await getQuestion(alreadyFeatures, params, this.state.answers);
      this.setState({ params: [...this.state.params, param], alreadyFeatures: [...this.state.alreadyFeatures, feature], answersButtons: answers, characterMatch, question, loading: false, finished: this.state.finished || !question });
    } catch(error) {
      console.log(error);
      this.setState({ loading: false });
      alert('Error on get Question');
    }
  }

  onButtonClick = async answer => {
    await this.setState({ answers: [...this.state.answers, answer] });
    await this.setQuestion();

    const finished = this.state.answers.length === numberOfQuestions;

    if(finished)
      this.setState({ finished: true });
  }

  render() {
    const { question, answersButtons, loading, finished, characterMatch } = this.state;

    return (
      <div className="app">
        <header>
          <h1 className='text-5xl'>FunTech!</h1>
          {/* <p>いくつかの簡単な質問に答えることで、絵日記を提案します！</p> */}
        </header>
        <TutorialModal />
        <main>
          { loading && !finished ? <h2>Carregando..</h2> : null }
          { !loading && !finished ? <SearchContainer question={question} answersButtons={answersButtons} onButtonClick={this.onButtonClick} /> : null }
          { finished ? <FinishedContainer characterMatch={characterMatch} /> : null }
        </main>
      </div>
    );
  }
}

export default App;