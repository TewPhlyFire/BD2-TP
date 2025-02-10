CREATE OR REPLACE FUNCTION atualizar_preco_produto()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se o produto já tem preço original salvo
    IF (SELECT COUNT(*) FROM Promo WHERE Id_Produto = NEW.Id_Produto AND Id_Promo != NEW.Id_Promo) = 0 THEN
        -- Salva o preço original apenas se não houver promoções anteriores
        UPDATE Produto
        SET Preco_original = Preco
        WHERE Id_Produto = NEW.Id_Produto;
    END IF;

    -- Atualiza o preço com desconto
    UPDATE Produto
    SET Preco = Preco_original * (1 - NEW.Desconto / 100)
    WHERE Id_Produto = NEW.Id_Produto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o trigger que chama a função ao inserir ou atualizar promoções
CREATE TRIGGER trg_atualizar_preco_produto
AFTER INSERT OR UPDATE ON Promo
FOR EACH ROW
EXECUTE FUNCTION atualizar_preco_produto();

CREATE OR REPLACE FUNCTION restaurar_preco_produto()
RETURNS TRIGGER AS $$
DECLARE
    tem_outras_promocoes INT;
BEGIN
    -- Verifica se existem outras promoções ativas para o mesmo produto
    SELECT COUNT(*) INTO tem_outras_promocoes FROM Promo WHERE Id_Produto = OLD.Id_Produto;

    IF tem_outras_promocoes = 0 THEN
        -- Restaura o preço original e zera o campo Preco_original
        UPDATE Produto
        SET Preco = Preco_original,
            Preco_original = 0
        WHERE Id_Produto = OLD.Id_Produto;
    END IF;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Criar o trigger que chama a função ao deletar promoções
CREATE TRIGGER trg_restaurar_preco_produto
AFTER DELETE ON Promo
FOR EACH ROW
EXECUTE FUNCTION restaurar_preco_produto();
