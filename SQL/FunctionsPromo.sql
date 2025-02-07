CREATE OR REPLACE FUNCTION aplicar_promocao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.Data_Inicio <= CURRENT_DATE AND NEW.Data_Fim >= CURRENT_DATE THEN
        UPDATE Produto
        SET preco_original = preco, 
            preco = preco - (preco * NEW.Desconto / 100)
        WHERE Id_Produto = NEW.Id_Produto;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_aplicar_promocao
AFTER INSERT OR UPDATE ON Promo
FOR EACH ROW
EXECUTE PROCEDURE aplicar_promocao();

CREATE OR REPLACE FUNCTION remover_promocao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.Data_Fim < CURRENT_DATE THEN
        UPDATE Produto
        SET preco = preco_original,
            preco_original = NULL
        WHERE Id_Produto = NEW.Id_Produto;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_remover_promocao
AFTER UPDATE ON Promo
FOR EACH ROW
WHEN (NEW.Data_Fim < CURRENT_DATE)
EXECUTE PROCEDURE remover_promocao();