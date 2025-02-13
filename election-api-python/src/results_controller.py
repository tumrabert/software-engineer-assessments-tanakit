from results_service import ResultStore
from typing import Dict, Any
class ResultsController:

    def __init__(self) -> None:
        self.store: ResultStore = ResultStore()
    
    def get_result(self, identifier: int) -> dict:
        return self.store.get_result(identifier)

    def new_result(self, result: dict) -> dict:
        self.store.new_result(result)
        return {}

    def reset(self) -> None:
        self.store.reset()

    def scoreboard(self) -> Dict[str, Any]:
        """
        Generates a scoreboard of election results.

        The scoreboard includes the number of seats, votes, and vote share for each party,
        as well as the overall winner if any party has secured the required number of seats.

        Returns:
            Dict[str, Any]: A dictionary containing the election results for each party and the overall winner.
            Example:
            {
                'CON': {'Seats': 0, 'Share': 0.22963810756005623, 'Votes': 36918},
                'GRN': {'Seats': 0, 'Share': 0.014119900974086561, 'Votes': 2270},
                'LAB': {'Seats': 4, 'Share': 0.40372964432778075, 'Votes': 64906},
                'LD': {'Seats': 1, 'Share': 0.22734906634487392, 'Votes': 36550},
                'OTH': {'Seats': 0, 'Share': 0.024999066966895984, 'Votes': 4019},
                'PC': {'Seats': 0, 'Share': 0.07368473433437418, 'Votes': 11846},
                'UKIP': {'Seats': 0, 'Share': 0.026479479491932374, 'Votes': 4257},
                'Winner': None
            }
        """
        scoreboard = {}
        results = self.store.get_all()

        #iterate through all results
        for result in results:
            for party_result in result['partyResults']:
                party_name = party_result['party']
                if party_name not in scoreboard:
                    scoreboard[party_name] = {"Seats": 0, "Votes": 0, "Share": 0.0}
                scoreboard[party_name]['Votes'] += party_result['votes']

            winning_party = max(result['partyResults'], key=lambda x: x['votes'])
            scoreboard[winning_party['party']]['Seats'] += 1

        total_votes = sum(party['Votes'] for party in scoreboard.values())
        for party in scoreboard.values():
            party['Share'] = party['Votes'] / total_votes if total_votes > 0 else 0.0

        winner_party = max(
            (party for party in scoreboard.items() if isinstance(party[1], dict)),
            key=lambda x: x[1]['Seats'],
            default=(None, None)
        )
        scoreboard['Winner'] = winner_party[0] if winner_party[1] and winner_party[1]['Seats'] >= 325 else None

        return scoreboard
