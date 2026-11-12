# InvoiceOne Identity Experience Login (`invoiceone_login`)

O módulo **InvoiceOne Identity Experience Login** personaliza a tela de autenticação do Odoo (**v15.0 a v20.0**), transformando o layout padrão numa experiência corporativa moderna dividida em duas colunas (*split-screen*), alinhada com a identidade visual da **DIGITALUB / InvoiceOne**.

## 🚀 Funcionalidades Principais

- **Layout Dividido (Split-Screen Premium)**:
  - **Painel Esquerdo (Funcional)**: Formulário de autenticação limpo com ícones SVG integrados nos campos, logótipo da marca, versão do sistema, estado dinâmico da licença/contrato e NIF da empresa.
  - **Painel Direito (Identidade Institucional)**: Painel estilizado com gradiente radial, nome dinâmico da empresa em maiúsculas, selo de certificação AGT e carrossel interativo de 3 slides.
- **Modo Produção & Modo Homologação**:
  - Inclui fita diagonal de canto (**HOMOLOGAÇÃO**) e faixa de alerta superior (*Ambiente de Testes / Homologação*) para identificação visual imediata de ambientes de teste e certificação.
- **Integração Automática com Gestão de Licenças (`db_license_manage`)**:
  - Exibe dinamicamente o estado do contrato (*Contrato Válido até DD/MM/AAAA*, *Contrato Expira a...* ou *Contrato Inativo*) quando o módulo `db_license_manage` está presente, funcionando também de forma autónoma.
- **Dados Corporativos Dinâmicos**:
  - Renderiza automaticamente o **Nome** e o **NIF (VAT)** da empresa ativa (`res.company`).

## 🖼️ Capturas de Ecrã

- **Vista de Produção**: `static/description/screenshot_prod.png`
- **Vista de Homologação / Testes**: `static/description/screenshot_hml.png`

## 📦 Compatibilidade

- **Versões Odoo**: `15.0`, `16.0`, `17.0`, `18.0`, `19.0` e `20.0` (Community & Enterprise)
- **Dependências Core**: `web`, `portal`
- **Licença**: OPL-1
- **Autor**: DIGITALUB ANGOLA, LDA (<https://www.digitalub.ao>)
