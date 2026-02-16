"""
Sobe um servidor HTTP na pasta allure-report para visualizar o relatório Allure.
Use quando você tiver a pasta allure-report (gerada localmente ou baixada do CI).

Uso:
  python scripts/serve_allure_report.py
  python scripts/serve_allure_report.py "C:/Users/.../Desktop/allure-report"   # pasta em outro lugar

Depois acesse no navegador: http://localhost:8800
"""
import http.server
import os
import sys

PORT = 8800


def main():
    if len(sys.argv) > 1:
        report_dir = os.path.abspath(sys.argv[1])
    else:
        # pasta do projeto = pai do diretório scripts
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        report_dir = os.path.join(project_root, "allure-report")

    if not os.path.isdir(report_dir):
        print(f"Pasta não encontrada: {report_dir}")
        print("Passe o caminho da pasta allure-report como argumento, ou gere o relatório antes:")
        print("  allure generate allure-results -o allure-report --clean")
        sys.exit(1)

    os.chdir(report_dir)
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", PORT), handler) as httpd:
        print(f"Relatório Allure em: http://localhost:{PORT}")
        print("Pressione Ctrl+C para encerrar.")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
