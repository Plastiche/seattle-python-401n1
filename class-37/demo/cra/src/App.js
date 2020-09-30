import React from "react";
import "./App.css";
import "./App.css";


export default function App() {
  let userName = "Darth Obvious";

  function getLocation() {
    return "Some Where over the Rainbow!";
  }

  function Header(props) {
    return (
      <header>
        <p>Hello {props.name2}, from the header of my page</p>
      </header>
    );
  }

  function Footer(props) {
    return (
      <footer>
        <p>Hello {props.name}, from the footer of my page</p>
      </footer>
    );
  }

  return (
    <>
      <Header name2="Will" />
      <div className="App">
        <h1>Hello {userName}</h1>
        {/*<h2>Start editing to see some magic happen!</h2>*/}
        <h2>{getLocation()}</h2>
      </div>
      <MoodToday mood='Sad'/>
      {/*<section>*/}
      {/*  <h3>This is an extra div</h3>*/}
      {/*</section>*/}
      {/*<Footer name="Roger" />*/}
      {/*<Footer name="Joe" />*/}
      <Footer name="Natalie" />
    </>
  );
}

class MoodToday extends React.Component {

  constructor() {
    super();
    this.state = {
      mood : 'neutral'
    }
  }

  changeMood(change) {
    this.setState({
      mood: 'Happy'
    })
  }

  render() {
    return (
      <>
        <button onClick={() => this.changeMood('improve')}>Improve</button>
        <button onClick={() => this.changeMood(('reduce'))}>Reduce</button>
        <h3>Today is a {this.state.mood} day!</h3>
      </>
    )
  }



}
