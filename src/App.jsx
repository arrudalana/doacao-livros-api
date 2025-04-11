import React from 'react';
import Header from './components/header/header';
import Footer from './components/footer/footer';
import DoacaoForm from './components/DoacaoForm';
import LivrosDoados from './components/LivrosDoados'; // Importe o componente LivrosDoados
import { DoacaoProvider } from './contexts/DoacaoContext'; // Importe o DoacaoProvider
import './GlobalStyle/globalStyle.scss';

function App() {
  return (
    <DoacaoProvider>
      <div className="App">
        <Header />
        <section id="doacao">
          <DoacaoForm />
        </section>
        <section id="livros-doados">
          <LivrosDoados /> 
        </section>
        <Footer />
      </div>
    </DoacaoProvider>
  );
}

export default App;