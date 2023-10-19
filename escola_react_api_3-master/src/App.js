import logo from './logo.svg';
import './App.css';
import ListaCursos from './components/listaCursos';
import Footer from './components/footer';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Nardoni Tech</h1>
        <p class="font-italic">Divisão de ensino</p>
        <h3>Cursos:</h3>
      </header>
      <ListaCursos/>
      <Footer/>
    </div>
  );
}

export default App;
