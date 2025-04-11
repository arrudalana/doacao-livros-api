import React from 'react';
    import DoacaoForm from '../../components/DoacaoForm';
    import styles from './QueroDoar.module.scss';
    import { enviarDoacao } from '../api';
    
    function QueroDoar() {
      return (
        <div className={styles.queroDoar}>
          <h2>Quero Doar</h2>
          <DoacaoForm />
        </div>
      );
    }
    
    export default QueroDoar;