--Trigger de atualização de Saldo de Caixa e de Quantidade de Produto no ato de inserção de Pedido
CREATE TRIGGER AtualizaCaixaEProduto
ON Pedido
AFTER INSERT
AS
BEGIN
    -- Atualizar o saldo da caixa com base no total do pedido
    UPDATE Caixa
    SET Saldo = Saldo + Inserted.Total
    FROM Caixa
    INNER JOIN Inserted ON Caixa.Id_Caixa = Inserted.Id_Caixa;

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
            THROW 50000, 'Operação abortada', 1;
            ROLLBACK;
        END
    ELSE
        BEGIN
            COMMIT;
        END   
    END     
END;
