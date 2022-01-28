import ordenador
import pytest
import contatempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        
        return ordenador.Ordenador()
        
    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = ContaTempos()
        return c.cria_lista(100)

    def ordenada(self,l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:

                return False
        return True
                
    
    def test_bolha_curta_aleat(self, o, l_aleat):
        o.bubble_short(l_aleat)
        assert self.ordenada(l_aleat)

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.ordenada(l_aleat)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bubble_short(l_quase)
        assert self.ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.ordenada(l_quase)
        
        
