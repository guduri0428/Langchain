from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("when will be the start date of IPL 2026?")

print(results)

# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/14.Tools/BuiltInTools (main)
# $ py duckduckgosearchtool.py 
# MORE: IPL 2026 squads: Complete squads for every Indian Premier League side. How to watch IPL 2026 mini-auction in India. The IPL mini-auction will be broadcast on the Star Sports network channels. Whereas, it will be live-streamed on Jio Hotstar's web and app. Time. IPL Auction 
# 2026 Date and Time: Another auction of the Indian Premier League is around the corner, which means another opportunity for all the 10 IPL teams to reinforce their squads and snap up a gamechanger of the future. 350 players will go under hammer for 77 spots at the 10 teams. Dubai: The Indian Premier League ( IPL ) 2026 mini-auction is set to take place on Tuesday, December 16, at the Etihad Arena in Abu Dhabi, marking the third consecutive year the auction will be held outside India. Today IPL Match Schedule 2025: Get full schedule of IPL 2025, Today IPL 
# Match with match timings, fixtures, time table, venues, dates , time, results and more on TOI.A total of 74 matches are expected to be played in IPL 2025. When will IPL 2025 start ? Check out the complete squad list for IPL 2026 ! Get the latest team updates, player rosters, and 
# squad details for all. Stay tuned for more at ESPNcricinfo.
# (.venv) 
# Lenovo@DESKTOP-GNHJGV0 MINGW64 /f/Gen AI Repos/Langchain/14.Tools/BuiltInTools (main)

search_tool2 = DuckDuckGoSearchResults()

results = search_tool2.invoke("when will be the start date of IPL 2026?")

print(results)