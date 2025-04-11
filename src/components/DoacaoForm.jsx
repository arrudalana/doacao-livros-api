import React, { useState, useContext } from 'react';
    import axios from 'axios';
    import { DoacaoContext } from '../contexts/DoacaoContext';
    import styles from './DoacaoForm.module.scss';
    import { buscarUsuarios } from '../api';
    
    function DoacaoForm() {
      const [titulo, setTitulo] = useState('');
      const [autor, setAutor] = useState('');
      const [genero, setGenero] = useState('');
      const { adicionarLivroDoado } = useContext(DoacaoContext);
    
      const handleSubmit = (event) => {
        event.preventDefault();
    
        axios
          .post('/api/doacao', { titulo, autor, genero })
          .then((response) => {
            console.log('Doação enviada com sucesso!', response.data);
            adicionarLivroDoado({ titulo, autor, genero });
            setTitulo('');
            setAutor('');
            setGenero('');
          })
          .catch((error) => {
            console.error('Erro ao enviar doação:', error);
          });
      };
    
      return (
        <form onSubmit={handleSubmit} className={styles.doacaoForm}>
          <input type="text" placeholder="Título" value={titulo} onChange={(e) => setTitulo(e.target.value)} />
          <input type="text" placeholder="Autor" value={autor} onChange={(e) => setAutor(e.target.value)} />
          <input type="text" placeholder="Gênero" value={genero} onChange={(e) => setGenero(e.target.value)} />
          <button type="submit">Doar</button>
        </form>
      );
    }
    
    export default DoacaoForm;