import axios from "axios";

const api = axios.create({
    baseURL:'http://127.0.0.1:5000'

});
export const enviarDoacao = (dadosDoacao) => {
  return api.post('/doacao', dadosDoacao);
};

export const buscarUsuarios = () => {
  return api.get('/users');
};

// Adicione outras funções de requisição conforme necessário

export default api