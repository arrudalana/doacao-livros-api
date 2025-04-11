import React from 'react';
    import styles from './LivroCard.module.scss';
    
    function LivroCard({ livro }) {
      return (
        <div className={styles.livroCard}>
          <h3>{livro.titulo}</h3>
          <p>Autor: {livro.autor}</p>
          <p>Gênero: {livro.genero}</p>
        </div>
      );
    }
    
    export default LivroCard;