-- Cómo se ve el movimiento en las tablas del banco
UPDATE cuentas SET saldo = saldo - 500 WHERE id = 'Cuenta_A';
UPDATE cuentas SET saldo = saldo + 500 WHERE id = 'Cuenta_B';
INSERT INTO historial (origen, destino, monto, fecha) VALUES ('A', 'B', 500, NOW());
