<!-- Interfaz visual simple -->
<div id="cajero">
    <h2>Transferencia Bancaria</h2>
    <input type="text" id="origen" placeholder="Cuenta Origen (A)">
    <input type="text" id="destino" placeholder="Cuenta Destino (B)">
    <input type="number" id="monto" placeholder="Cantidad $">
    <button onclick="enviarTransferencia()">Confirmar Envío</button>
</div>

<script>
async function enviarTransferencia() {
    const datos = {
        desde: document.getElementById('origen').value,
        hacia: document.getElementById('destino').value,
        cantidad: parseFloat(document.getElementById('monto').value)
    };

    // Esto envía los datos al "Cerebro" (Servidor)
    const respuesta = await fetch('https://api.mibanco.com', {
        method: 'POST',
        body: JSON.stringify(datos)
    });
    
    const resultado = await respuesta.json();
    alert(resultado.mensaje);
}
</script>
