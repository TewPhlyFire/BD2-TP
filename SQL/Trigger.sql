--Trigger de atualização de Quantidade de Produto no ato de inserção de Pedido
CREATE TRIGGER AtualizaStockEProduto
ON Pedido
AFTER INSERT
AS
BEGIN
       -- Atualizar a quantidade do produto com base na quantidade do pedido
    UPDATE Produto
    SET Quantidade = Quantidade - Inserted.Quantidade
    FROM Produto
    INNER JOIN Inserted ON Produto.Id_Produto = Inserted.Id_Produto;

    -- Verificar se as atualizações causaram problemas (quantidades negativas)
    IF EXISTS 
    (
        SELECT Produto.Quantidade
        FROM Produto
        INNER JOIN Inserted ON Inserted.Id_Produto = Produto.Id_Produto
        WHERE Produto.Quantidade < 0
    )
        BEGIN
        ROLLBACK TRANSACTION;
        THROW 50000, 'Operação abortada', 1;
    END
END;
/*
se nao funcionar usar este
CREATE OR REPLACE FUNCTION AtualizaCaixaEProduto()
RETURNS TRIGGER AS
$$
BEGIN
    -- Atualizar o saldo da caixa com base no total do pedido
    UPDATE Caixa
    SET Saldo = Saldo + NEW.Total
    WHERE Id_Caixa = NEW.Id_Caixa;

    -- Atualizar a quantidade do produto com base na quantidade do pedido
    UPDATE Produto
    SET Quantidade = Quantidade - NEW.Quantidade
    WHERE Id_Produto = NEW.Id_Produto;

    -- Verificar se a quantidade do produto ficou negativa
    IF EXISTS (
        SELECT 1
        FROM Produto
        WHERE Id_Produto = NEW.Id_Produto AND Quantidade < 0
    ) THEN
        -- Se a quantidade ficou negativa, desfaz a transação
        RAISE EXCEPTION 'Operação abortada: Quantidade de produto não pode ser negativa';
    END IF;

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

-- Criando o trigger para a tabela Pedido
CREATE TRIGGER AtualizaCaixaEProduto
AFTER INSERT ON Pedido
FOR EACH ROW
EXECUTE FUNCTION AtualizaCaixaEProduto();
*/