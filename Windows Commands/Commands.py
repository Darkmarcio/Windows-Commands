Windows Commands 

Comandos Básicos do Sistema
dir - Lista os arquivos e pastas no diretório atual.

cd - Altera o diretório atual.

Exemplo: cd C:\Pasta ou cd .. (volta um nível).

cls - Limpa a tela do CMD.

exit - Fecha o Prompt de Comando.

help - Exibe uma lista de comandos disponíveis.

Exemplo: help dir (mostra ajuda sobre o comando dir).

ver - Exibe a versão do Windows.

systeminfo - Exibe informações detalhadas sobre o sistema.

hostname - Mostra o nome do computador.

time - Exibe ou altera a hora do sistema.

date - Exibe ou altera a data do sistema.

Comandos de Arquivos e Pastas
copy - Copia arquivos de um local para outro.

Exemplo: copy arquivo.txt C:\Pasta.

xcopy - Copia arquivos e diretórios, incluindo subdiretórios.

Exemplo: xcopy C:\Origem C:\Destino /s.

move - Move arquivos ou pastas para outro local.

Exemplo: move arquivo.txt C:\Pasta.

del - Exclui um ou mais arquivos.

Exemplo: del arquivo.txt.

rmdir ou rd - Remove um diretório.

Exemplo: rmdir Pasta.

mkdir ou md - Cria um novo diretório.

Exemplo: mkdir NovaPasta.

type - Exibe o conteúdo de um arquivo de texto.

Exemplo: type arquivo.txt.

attrib - Altera atributos de arquivos ou pastas (oculto, somente leitura, etc.).

Exemplo: attrib +h arquivo.txt (oculta o arquivo).

tree - Exibe a estrutura de diretórios em forma de árvore.

Exemplo: tree C:\Pasta.

Comandos de Rede
ipconfig - Exibe informações de rede (IP, gateway, etc.).

Exemplo: ipconfig /all.

ping - Testa a conectividade com outro dispositivo na rede.

Exemplo: ping google.com.

tracert - Rastreia o caminho dos pacotes até um destino.

Exemplo: tracert google.com.

netstat - Exibe conexões de rede e portas abertas.

Exemplo: netstat -an.

nslookup - Consulta informações de DNS.

Exemplo: nslookup google.com.

netsh - Configurações avançadas de rede.

Exemplo: netsh wlan show profiles (mostra redes Wi-Fi salvas).

arp - Exibe a tabela ARP (mapeamento de IP para MAC).

Exemplo: arp -a.

Comandos de Gerenciamento de Disco
chkdsk - Verifica e repara erros no disco.

Exemplo: chkdsk C: /f.

diskpart - Ferramenta avançada de gerenciamento de discos.

Exemplo: diskpart (abre o utilitário).

format - Formata um disco ou partição.

Exemplo: format D:.

defrag - Desfragmenta um disco.

Exemplo: defrag C:.

Comandos de Processos e Serviços
tasklist - Lista os processos em execução.

Exemplo: tasklist.

taskkill - Encerra um processo.

Exemplo: taskkill /im notepad.exe.

sc - Gerencia serviços do Windows.

Exemplo: sc query (lista serviços).

shutdown - Desliga ou reinicia o computador.

Exemplo: shutdown /s (desliga) ou shutdown /r (reinicia).

start - Inicia um programa ou comando.

Exemplo: start notepad.exe.

Comandos de Script e Automação
echo - Exibe uma mensagem ou ativa/desativa o eco de comandos.

Exemplo: echo Olá, Mundo!.

set - Exibe ou define variáveis de ambiente.

Exemplo: set PATH.

for - Executa um comando para cada item em uma lista.

Exemplo: for %i in (*.txt) do echo %i.

if - Executa comandos condicionalmente.

Exemplo: if exist arquivo.txt echo Existe.

goto - Direciona a execução para um rótulo em um script.

Exemplo: goto inicio.

Comandos Avançados
sfc /scannow - Verifica e repara arquivos do sistema.

dism - Ferramenta de manutenção de imagens do Windows.

Exemplo: dism /online /cleanup-image /restorehealth.

wmic - Acessa informações do sistema via WMI.

Exemplo: wmic cpu get name (mostra o nome do processador).

reg - Manipula o registro do Windows.

Exemplo: reg query HKLM\Software.

schtasks - Agenda tarefas no Windows.

Exemplo: schtasks /create /tn "Tarefa" /tr "notepad.exe" /sc daily.

Comandos de Segurança
cipher - Criptografa ou descriptografa arquivos.

Exemplo: cipher /e arquivo.txt.

net user - Gerencia contas de usuário.

Exemplo: net user NomeDoUsuario.

net localgroup - Gerencia grupos de usuários.

Exemplo: net localgroup Administradores.

Comandos de Desempenho
perfmon - Abre o Monitor de Desempenho.

typeperf - Exibe dados de desempenho em tempo real.

Exemplo: typeperf "\Processor(_Total)\% Processor Time".

Comandos de Rede Adicionais
route - Exibe ou modifica a tabela de roteamento.

Exemplo: route print.

telnet - Conecta a um servidor remoto via Telnet (não vem habilitado por padrão no Windows).

Exemplo: telnet exemplo.com 80.

ftp - Conecta a um servidor FTP para transferência de arquivos.

Exemplo: ftp exemplo.com.

netsh interface - Configura interfaces de rede.

Exemplo: netsh interface ip show config.

pathping - Combina ping e tracert para diagnosticar problemas de rede.

Exemplo: pathping google.com.

Comandos de Gerenciamento de Energia
powercfg - Gerencia configurações de energia.

Exemplo: powercfg /energy (gera um relatório de eficiência energética).

powercfg /hibernate on - Ativa a hibernação.

powercfg /hibernate off - Desativa a hibernação.

Comandos de Script e Automação Adicionais
call - Chama um script ou comando de outro arquivo de lote.

Exemplo: call script.bat.

pause - Pausa a execução de um script e espera uma tecla ser pressionada.

choice - Permite a seleção de opções em um script.

Exemplo: choice /c YN /m "Deseja continuar?".

find - Procura uma string em um arquivo ou saída de comando.

Exemplo: find "palavra" arquivo.txt.

findstr - Similar ao find, mas com suporte a expressões regulares.

Exemplo: findstr "palavra" *.txt.

Comandos de Gerenciamento de Disco Adicionais
vssadmin - Gerencia o Volume Shadow Copy Service.

Exemplo: vssadmin list shadows.

fsutil - Ferramenta avançada para gerenciamento de sistemas de arquivos.

Exemplo: fsutil file createnew arquivo.txt 1024 (cria um arquivo de 1 KB).

mountvol - Gerencia pontos de montagem de volumes.

Exemplo: mountvol.

Comandos de Segurança Adicionais
cacls ou icacls - Gerencia permissões de arquivos e pastas.

Exemplo: icacls arquivo.txt /grant Usuário:(R,W).

auditpol - Configura políticas de auditoria de segurança.

Exemplo: auditpol /get /category:*.

gpupdate - Atualiza políticas de grupo.

Exemplo: gpupdate /force.

gpresult - Exibe o resultado das políticas de grupo aplicadas.

Exemplo: gpresult /r.

Comandos de Desempenho e Diagnóstico
logman - Gerencia coletores de dados de desempenho.

Exemplo: logman create counter coleta -o log.csv -c "\Processor(_Total)\% Processor Time".

typeperf - Exibe dados de desempenho em tempo real.

Exemplo: typeperf "\Memory\Available MBytes".

winsat - Avalia o desempenho do sistema.

Exemplo: winsat formal.

Comandos de Gerenciamento de Usuários e Grupos
net group - Gerencia grupos de usuários.

Exemplo: net group Administradores.

net accounts - Exibe ou altera configurações de contas de usuário.

Exemplo: net accounts.

net share - Gerencia compartilhamentos de rede.

Exemplo: net share.

Comandos de Gerenciamento de Impressoras
print - Envia um arquivo para a impressora.

Exemplo: print arquivo.txt.

net print - Gerencia trabalhos de impressão.

Exemplo: net print \\Servidor\Impressora.

Comandos de Gerenciamento de Serviços
net start - Inicia um serviço.

Exemplo: net start Spooler.

net stop - Para um serviço.

Exemplo: net stop Spooler.

net pause - Pausa um serviço.

Exemplo: net pause Spooler.

net continue - Continua um serviço pausado.

Exemplo: net continue Spooler.

Comandos de Gerenciamento de Sessões
query session - Exibe sessões ativas no sistema.

Exemplo: query session.

query user - Exibe usuários conectados.

Exemplo: query user.

logoff - Desconecta um usuário.

Exemplo: logoff 1 (desconecta a sessão 1).

Comandos de Gerenciamento de Arquivos de Log
wevtutil - Gerencia logs de eventos do Windows.

Exemplo: wevtutil qe System /f:text.

eventcreate - Cria um evento personalizado no log de eventos.

Exemplo: eventcreate /t ERROR /id 100 /l APPLICATION /d "Erro crítico".

Comandos de Gerenciamento de Drivers
driverquery - Lista os drivers instalados no sistema.

Exemplo: driverquery.

pnputil - Gerencia drivers de dispositivos.

Exemplo: pnputil /enum-drivers.

Comandos de Gerenciamento de Memória
wmic memorychip - Exibe informações sobre módulos de memória.

Exemplo: wmic memorychip get capacity, speed.

Comandos de Gerenciamento de BIOS
wmic bios - Exibe informações sobre a BIOS.

Exemplo: wmic bios get serialnumber.

Comandos de Gerenciamento de Atualizações
wuauclt - Força a verificação de atualizações do Windows.

Exemplo: wuauclt /detectnow.

Comandos de Gerenciamento de Virtualização
vmconnect - Conecta a uma máquina virtual Hyper-V.

Exemplo: vmconnect localhost "NomeDaVM".

mstsc - Abre o cliente de Área de Trabalho Remota.

Exemplo: mstsc.

Comandos de Gerenciamento de Firewall
netsh advfirewall - Configura o Firewall do Windows.

Exemplo: netsh advfirewall show allprofiles.