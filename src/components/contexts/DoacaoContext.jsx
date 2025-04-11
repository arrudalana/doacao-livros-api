import React, { createContext, useState } from 'react';
    
    export const DoacaoContext = createContext();
    
    export const DoacaoProvider = ({ children }) => {
      const [livrosDoados, setLivrosDoados] = useState([]);
    
      const adicionarLivroDoado = (livro) => {
        setLivrosDoados([...livrosDoados, livro]);
      };
    
      return (
        <DoacaoContext.Provider value={{ livrosDoados, adicionarLivroDoado }}>
          {children}
        </DoacaoContext.Provider>
      );
    };