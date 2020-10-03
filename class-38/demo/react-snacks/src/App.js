import React from 'react';
// import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      snacks: [
        {
          id: 1,
          name: 'twix',
          type: 'candy',
        },
        {
          id: 2,
          name: 'snickers',
          type: 'candy',
        }
      ],
      popularSnack: 'Nothing yet'
    }
  }

  render() {
    return (
      <div className="App">
        <Header snacks={this.state.snacks}/>
        <main>
          <SnackList snacks={this.state.snacks} onSnackCreate={(snack) => alert(snack.name)}/>
        </main>
        <Footer footerText="This is the new Footer"/>
      </div>
    )
  }
}

function Header(props) {
  return(
    <h2>The number of snacks are: {props.snacks.length}</h2>
  )
}

function Footer(props) {
  return(
    <footer><small>{props.footerText}</small></footer>
  )
}

function SnackList(props){
  return(
    <>
    <h2>Snack List</h2>
      <ul>
        {props.snacks.map(snack => <Snack item={snack} key={snack.id}/>)}
      </ul>
      {/*{props.onSnackCreate()}*/}
      <SnackForm onSnackCreate={props.onSnackCreate}/>
      {/*<button>Add New Snack</button>*/}
      </>
  )
}

class SnackForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name: '',
      snackType: '',
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
    let newName = event.target.value;
    this.setState(({
      name: newName
    }))
  }

  handleSubmit(event){
    event.preventDefault();
    this.props.onSnackCreate(this.state)
  }

  render(){
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.name} onChange={this.handleChange}/>
        </label>
      </form>
    )
  }
}

function Snack(props) {
  return <li>A snack I have access to is: {props.item.name}</li>
}

export default App;
