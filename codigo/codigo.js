function validar() {
    let cpfDigitado = document.getElementById("cpf").value;
    let validado = false;
    let isFirstDigitOn = false;
    let vezes = 0;
    if (cpfDigitado.length > 11) {
        alert("Digite um CPF no formato numérico de CPF. (Sem pontos, traços e com 11 dígitos.)");
    }
    else {
        let resultado = [];
        let cpfCortado;
        let aux;
        let penultimo;
        let ultimo;

        while (!validado) {
            if (!isFirstDigitOn) {
                cpfCortado = cpfDigitado.slice(0, 9);
                aux = 10;
            }
            else {
                cpfCortado = cpfDigitado.slice(0, 10);
                aux = 11;
            }

            for (let i = 0; i < cpfCortado.length; i++) {
                resultado.push(cpfCortado[i] * aux);
                aux--;
            }
            console.log(resultado);

            function soma() {
                let sum = 0;
                for (let i = 0; i < resultado.length; i++) {
                    sum += resultado[i];
                }
                return sum;
            }


            if (soma() % 11 >= 2) {
                if (!isFirstDigitOn) {
                    penultimo = 11 - (soma() % 11);
                    cpfCortado += toString(penultimo);
                    resultado = [];
                    isFirstDigitOn = true;
                }
                else {
                    ultimo = 11 - (soma() % 11);
                }

            }
            else {
                if (!isFirstDigitOn) {
                    penultimo = 0;
                    cpfCortado += toString(penultimo);
                    resultado = [];
                    isFirstDigitOn = true;
                }
                else {
                    ultimo = 0;
                }
            }
            vezes++;


            if (penultimo == cpfDigitado[9] && ultimo == cpfDigitado[10]) {
                if (vezes == 2) {
                    validado = true;
                    alert("Seu CPF é valido!!");
                }
            }
            else {
                if (vezes == 2) {
                    alert("Seu CPF é inválido.");
                    break;
                }
            }
        }
    }
}