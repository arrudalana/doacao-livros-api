import React, { useContext } from 'react';
    import LivroCard from '../../components/LivroCard';
    import { DoacaoContext } from '../../contexts/DoacaoContext';
    import styles from './LivrosDoados.module.scss';
    
    
    function LivrosDoados() {
      const { livrosDoados } = useContext(DoacaoContext);
    
      return (
        <div className={styles.livrosDoados}>
          <h2>Livros Doados</h2>
          <div className={styles.cardList}>
            {livrosDoados.map((livro, index) => (
              <LivroCard key={index} livro={livro} />
            ))}
          </div>
        </div>
      );
    }
    
    export default LivrosDoados;