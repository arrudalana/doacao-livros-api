import { Link } from 'react-router-dom';
    import logoLivro from '../../assets/logoLivro.png';
    import lupa from '../../assets/lupa.png';
    import s from './header.module.scss';
    
    export default function Header() {
      return (
        <header className={s.header}>
          <section className={s.logoHeader}>
            <img
              src={logoLivro}
              alt="Imagem de ilustração de livro aberto com capa azul"
            />
            <h1>Livros Vai na Web</h1>
          </section>
          <nav className={s.navHeader}>
            <ul>
              <li>
                <Link className={s.link} to="/">
                  Início
                </Link>
              </li>
              <li>
                <Link className={s.link} to="/livrosdoados">
                  Livros Doados
                </Link>
              </li>
              <li>
                <Link className={s.link} to="/querodoar">
                  Quero Doar
                </Link>
              </li>
            </ul>
          </nav>
          <nav className={s.barraDeBusca}>
            <input
              type="search"
              name="busca"
              id="busca"
              placeholder="O que você procura?"
              aria-label="Campo de busca"
            />
            <button aria-label="Buscar">
              <img src={lupa} alt="Icone de lupa branca" />
            </button>
          </nav>
        </header>
      );
    }