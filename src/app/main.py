import argparse
from .graph import build_app

def cli():
    parser = argparse.ArgumentParser(description="Lang Ecosystem Starter")
    parser.add_argument(
        "-q", "--query", required=False,
        default="Avaliar DQ de duplicidades em base de clientes e propor próximos passos.",
        help="Pergunta/consulta de entrada"
    )
    args = parser.parse_args()

    app = build_app()
    state = {
        "consulta": args.query,
        "artefatos": {},
        "log": []
    }
    final_state = app.invoke(state)

    print("\n=== Resultado ===")
    print(final_state["artefatos"])
    print("\n=== Log ===")
    for l in final_state["log"]:
        print("-", l)

if __name__ == "__main__":
    cli()
