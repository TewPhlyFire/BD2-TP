-- Delete
DELETE FROM Pedido
DELETE FROM Produto
DELETE FROM Categoria
DELETE FROM Caixa
DELETE FROM Funcionario
DELETE FROM Cliente


--Cliente
INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client)
VALUES (123456789, 'João', 'Silva', '912345678', 'Rua das Flores, 123', 'joao.silva@email.com', 'senhaSegura123');

INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client) 
VALUES (987654321, 'John', 'Doe', '123-456-7890', '123 Main St', 'johndoe@example.com', 'securepassword');

INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client)
VALUES (456789123, 'Ana', 'Pereira', '915678432', 'Av. Central, 45', 'ana.pereira@mail.com', 'anaPassword456');

INSERT INTO Cliente (NIF_Cliente, PNome_Cliente, UNome_Cliente, Contacto_Tel, Morada, Mail, Password_Client)
VALUES (789123456, 'Carlos', 'Martins', '916543210', 'Rua do Sol, 88', 'carlos.martins@mail.com', 'carlos123');

--Funcionario
INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario)
VALUES ('Maria', 'Santos');

INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario)
VALUES ('Orlando', 'Jesus');

INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario)
VALUES ('Pedro', 'Oliveira');

INSERT INTO Funcionario (PNome_Funcionario, UNome_Funcionario)
VALUES ('Inês', 'Gomes');

--Categoria e Subcategoria
INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (NULL, 'Eletrônicos');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (1, 'Telemoveis');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (1, 'Computadores');

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (NULL, 'Bebidas')

INSERT INTO Categoria (Id_Categoria_Parent, Nome_Categoria)
VALUES (2, 'Energéticas');

--Caixa
INSERT INTO Caixa (Saldo)
VALUES (123);

INSERT INTO Caixa (Saldo)
VALUES (500.75);

INSERT INTO Caixa (Saldo)
VALUES (1000.50);

INSERT INTO Caixa (Saldo)
VALUES (250.00);

--Produto
INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Sony Xperia 5', 'Smartphone com 128GB e 6GB RAM', 489.99, 2, 8);

INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Microsoft Surface Pro 7 Plus', 'Tablet com teclado destacável e 256GB SSD', 850.00, 3, 2);

INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('Red Bull 25cl', 'Bebida energética', 1.50, 5, 10);

INSERT INTO Produto (Nome_Produto, Descricao, Preco_Produto, Id_Categoria_Parent, Quantidade)
VALUES ('iPhone 13', '128GB, Cor Azul', 999.99, 2, 5);

--Pedido
INSERT INTO Pedido (Id_Produto, Data_Hora, Quantidade, Total, NIF_Cliente, Id_Funcionario, Id_Caixa)
VALUES (1, GETDATE(), 2, 979.98, 123456789, 1, 1);

INSERT INTO Pedido (Id_Produto, Data_Hora, Quantidade, Total, NIF_Cliente, Id_Funcionario, Id_Caixa)
VALUES (2, GETDATE(), 1, 850.00, 987654321, 2, 2);

INSERT INTO Pedido (Id_Produto, Data_Hora, Quantidade, Total, NIF_Cliente, Id_Funcionario, Id_Caixa)
VALUES (3, GETDATE(), 6, 9.00, 456789123, 3, 3);

INSERT INTO Pedido (Id_Produto, Data_Hora, Quantidade, Total, NIF_Cliente, Id_Funcionario, Id_Caixa)
VALUES (4, GETDATE(), 1, 999.99, 789123456, 1, 4);