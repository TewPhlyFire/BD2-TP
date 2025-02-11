-- Inserir na tabela Cliente
INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client)
VALUES
(123456789, 'João', 'Silva', '912345678', 'Rua A, 123', 'joao.silva@email.com', 'senha123'),
(987654321, 'Maria', 'Santos', '913456789', 'Rua B, 456', 'maria.santos@email.com', 'senha456'),
(112233445, 'Carlos', 'Pereira', '914567890', 'Rua C, 789', 'carlos.pereira@email.com', 'senha789'),
(998877665, 'Ana', 'Costa', '915678901', 'Rua D, 101', 'ana.costa@email.com', 'senha101');

-- Inserir na tabela Funcionario
INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario, Senha_Funcionario)
VALUES
('Paulo', 'Ferreira', 'senhaPaulo123'),
('Laura', 'Oliveira', 'senhaLaura456'),
('José', 'Mendes', 'senhaJose789'),
('Raquel', 'Martins', 'senhaRaquel101');

-- Inserir na tabela Categoria
INSERT INTO Categoria (Id_subcategoria, Nome_Categoria)
VALUES
(NULL, 'Eletrônicos'),
(1, 'Móveis'),
(2, 'Alimentos'),
(3, 'Vestuário');

-- Inserir na tabela Produto
INSERT INTO Produto (Nome_Produto, Descricao, Preco_original, Preco, Id_subcategoria, Quantidade)
VALUES
('Smartphone', 'Celular com tela de 6.5"', 500.00, 500.00, 1, 10),
('Sofá', 'Sofá de 3 lugares', 300.00, 300.00, 2, 5),
('Arroz', 'Pacote de arroz 5kg', 10.00, 10.00, 3, 50),
('Camiseta', 'Camiseta de algodão', 25.00, 25.00, 4, 20);


-- Inserir na tabela Promo
INSERT INTO Promo (Id_Produto, Data_Inicio, Data_Fim, Desconto)
VALUES
(1, '2025-02-01', '2025-02-28', 10.00),
(2, '2025-02-01', '2025-02-28', 15.00),
(3, '2025-02-01', '2025-02-28', 5.00),
(4, '2025-02-01', '2025-02-28', 20.00);