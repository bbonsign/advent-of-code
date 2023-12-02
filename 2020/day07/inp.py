test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

inp = """dark olive bags contain 2 muted brown bags, 1 mirrored tomato bag, 4 bright black bags.
faded coral bags contain 3 drab cyan bags, 1 light aqua bag.
plaid plum bags contain 2 mirrored cyan bags.
clear maroon bags contain 1 dotted turquoise bag, 3 dim lavender bags.
plaid coral bags contain 3 posh fuchsia bags, 3 dotted beige bags, 2 wavy turquoise bags.
mirrored indigo bags contain 5 pale orange bags, 5 striped aqua bags, 1 dotted cyan bag, 4 muted coral bags.
striped brown bags contain 4 faded green bags, 5 vibrant red bags, 3 drab black bags, 3 dark orange bags.
drab fuchsia bags contain 5 shiny chartreuse bags, 1 dark orange bag, 4 drab blue bags, 1 bright chartreuse bag.
light fuchsia bags contain 3 bright gold bags, 5 clear indigo bags.
plaid olive bags contain 4 striped indigo bags, 4 muted olive bags, 2 light gray bags, 2 wavy purple bags.
dotted green bags contain 2 faded yellow bags.
dotted cyan bags contain 1 light red bag, 5 dark cyan bags.
muted magenta bags contain 2 clear plum bags.
mirrored cyan bags contain 4 bright lavender bags, 3 mirrored gold bags, 2 plaid silver bags, 1 posh chartreuse bag.
muted red bags contain 2 wavy olive bags, 4 shiny cyan bags.
clear indigo bags contain 2 dotted magenta bags, 4 bright silver bags, 4 muted aqua bags.
plaid chartreuse bags contain 3 dark chartreuse bags, 1 faded lavender bag.
wavy tan bags contain 3 light red bags.
bright crimson bags contain 4 pale magenta bags.
pale yellow bags contain 3 clear plum bags, 2 vibrant cyan bags, 2 muted white bags.
pale tomato bags contain 2 muted red bags.
dull salmon bags contain 3 dark gold bags.
light white bags contain 2 drab chartreuse bags.
drab plum bags contain 1 dark brown bag.
shiny purple bags contain 3 pale brown bags, 1 bright crimson bag, 5 muted teal bags.
pale red bags contain 5 posh cyan bags, 2 drab cyan bags.
dull bronze bags contain 2 striped indigo bags, 4 plaid black bags, 3 clear violet bags, 1 dull chartreuse bag.
wavy indigo bags contain 2 dull coral bags, 1 dark tan bag.
vibrant silver bags contain 5 muted aqua bags.
shiny tan bags contain 4 pale beige bags, 4 bright gold bags, 5 muted coral bags, 3 shiny red bags.
dim yellow bags contain 1 dotted chartreuse bag.
faded white bags contain 5 posh lavender bags, 3 bright silver bags, 2 dark green bags, 5 muted lavender bags.
shiny tomato bags contain 4 mirrored chartreuse bags, 2 bright yellow bags, 4 vibrant plum bags.
dark yellow bags contain 3 plaid lime bags, 4 wavy lavender bags.
dim magenta bags contain 3 wavy violet bags.
striped white bags contain 5 striped chartreuse bags.
muted gray bags contain 5 muted brown bags, 5 light lavender bags, 2 clear gold bags, 1 shiny green bag.
drab white bags contain 4 muted yellow bags, 3 posh lavender bags, 3 faded fuchsia bags.
dark lime bags contain 1 bright crimson bag.
muted salmon bags contain 4 dull red bags, 1 dull violet bag.
muted black bags contain 2 vibrant black bags, 5 pale tomato bags.
plaid white bags contain 4 drab black bags, 4 drab cyan bags, 1 dim olive bag.
clear green bags contain 3 wavy purple bags, 1 pale gold bag.
drab orange bags contain 4 clear maroon bags, 3 vibrant gold bags.
light salmon bags contain 1 pale black bag, 2 posh fuchsia bags.
faded tomato bags contain 5 faded black bags, 3 vibrant coral bags, 3 bright brown bags.
dull green bags contain 5 clear lime bags.
dim orange bags contain 5 posh red bags, 2 dim gray bags, 2 muted gold bags.
dotted orange bags contain 1 faded tan bag, 2 drab tomato bags.
dull gold bags contain 5 muted gold bags.
clear beige bags contain 5 plaid tan bags, 4 dim maroon bags.
mirrored bronze bags contain 1 clear blue bag, 2 clear tan bags, 3 clear orange bags.
shiny brown bags contain 5 light tomato bags.
pale cyan bags contain 3 dull silver bags.
muted purple bags contain 4 posh brown bags.
pale maroon bags contain 1 clear maroon bag, 5 vibrant yellow bags, 1 shiny violet bag.
muted green bags contain 5 plaid plum bags.
light coral bags contain 5 bright lime bags, 1 dotted indigo bag, 5 shiny bronze bags.
wavy beige bags contain 5 light magenta bags, 3 pale lime bags, 1 faded yellow bag.
wavy turquoise bags contain 5 shiny red bags, 3 mirrored yellow bags, 2 posh bronze bags.
pale brown bags contain 2 striped salmon bags, 4 vibrant plum bags, 2 dull silver bags.
striped bronze bags contain 3 posh black bags, 2 bright yellow bags, 3 dotted silver bags, 1 mirrored violet bag.
pale tan bags contain 4 shiny lavender bags, 3 dotted turquoise bags, 3 pale turquoise bags, 5 plaid white bags.
muted crimson bags contain 4 dull lime bags, 4 pale magenta bags, 2 light cyan bags.
dotted purple bags contain 2 wavy magenta bags.
dull black bags contain 3 light crimson bags, 3 mirrored fuchsia bags, 3 posh lime bags.
mirrored aqua bags contain 1 dark brown bag, 5 pale gold bags, 2 pale purple bags, 2 vibrant crimson bags.
shiny beige bags contain 2 muted indigo bags, 2 dark tan bags.
shiny aqua bags contain 5 vibrant tan bags, 2 pale tomato bags, 2 faded blue bags, 4 pale magenta bags.
mirrored lavender bags contain 4 faded yellow bags, 3 light chartreuse bags, 2 dull crimson bags, 1 pale aqua bag.
faded gray bags contain 5 bright yellow bags, 4 light silver bags.
light tan bags contain 3 bright fuchsia bags, 3 light crimson bags, 3 clear olive bags, 1 clear silver bag.
dull crimson bags contain 3 wavy olive bags, 1 light maroon bag.
pale olive bags contain 4 vibrant purple bags, 3 clear fuchsia bags, 2 pale tan bags.
dim beige bags contain 3 dull silver bags.
dark bronze bags contain 1 mirrored orange bag, 2 wavy crimson bags, 1 dark maroon bag.
mirrored fuchsia bags contain 1 dark chartreuse bag, 1 dotted bronze bag, 5 shiny silver bags.
striped tomato bags contain 1 dark fuchsia bag, 5 vibrant maroon bags, 4 drab crimson bags.
muted chartreuse bags contain 1 light tomato bag, 3 light magenta bags, 3 dull beige bags.
muted violet bags contain 5 light tomato bags.
dim violet bags contain 2 mirrored purple bags, 3 bright black bags, 5 vibrant plum bags.
muted beige bags contain 4 muted plum bags, 4 mirrored gold bags, 5 bright yellow bags.
shiny coral bags contain 5 vibrant gray bags, 1 light bronze bag, 5 faded chartreuse bags, 2 plaid violet bags.
dotted yellow bags contain 5 dotted turquoise bags.
faded bronze bags contain 4 dull purple bags, 2 pale fuchsia bags.
clear fuchsia bags contain 5 bright yellow bags.
dotted beige bags contain 1 pale turquoise bag.
bright aqua bags contain 2 faded silver bags, 5 dim fuchsia bags.
dim silver bags contain 5 wavy brown bags, 1 light maroon bag, 2 wavy black bags.
plaid tan bags contain 3 dotted green bags.
drab teal bags contain 4 mirrored violet bags, 5 dotted bronze bags, 1 pale cyan bag.
plaid yellow bags contain 5 shiny magenta bags, 1 dark silver bag, 5 shiny indigo bags, 3 faded gray bags.
dull cyan bags contain 1 posh plum bag, 5 dim coral bags.
pale beige bags contain 3 dark cyan bags, 4 faded tan bags, 2 plaid silver bags.
faded salmon bags contain 2 light olive bags, 2 dark tan bags.
bright silver bags contain 1 clear fuchsia bag, 2 clear lime bags.
dark lavender bags contain 1 pale cyan bag, 5 dotted salmon bags, 1 striped turquoise bag, 2 dim crimson bags.
light gray bags contain 3 dotted chartreuse bags, 3 dull red bags, 4 bright gold bags, 2 light lime bags.
dark indigo bags contain 5 shiny coral bags, 1 muted teal bag, 2 plaid purple bags, 4 faded yellow bags.
light maroon bags contain 1 wavy brown bag.
dotted brown bags contain 1 clear violet bag.
pale indigo bags contain 1 wavy brown bag, 2 dark olive bags, 4 pale black bags, 5 striped lavender bags.
pale purple bags contain 5 bright chartreuse bags, 1 vibrant magenta bag, 4 clear tomato bags, 4 light cyan bags.
dim teal bags contain 2 dark salmon bags, 5 mirrored gold bags, 3 bright gold bags.
wavy olive bags contain 1 vibrant purple bag, 3 dull silver bags.
pale aqua bags contain 4 dark violet bags, 2 dark plum bags, 3 vibrant brown bags.
muted cyan bags contain 5 vibrant crimson bags, 3 pale magenta bags.
vibrant fuchsia bags contain 2 light beige bags, 5 bright purple bags, 3 light maroon bags, 4 dull beige bags.
bright blue bags contain 4 vibrant plum bags.
vibrant green bags contain 1 dark salmon bag.
dull red bags contain 2 dotted maroon bags, 1 posh salmon bag, 3 dotted chartreuse bags, 2 dim yellow bags.
dotted magenta bags contain 3 plaid violet bags, 3 light gray bags.
wavy bronze bags contain 1 posh plum bag, 2 bright lavender bags.
shiny orange bags contain 3 muted plum bags.
plaid bronze bags contain 5 plaid chartreuse bags, 3 mirrored turquoise bags, 3 light salmon bags.
shiny yellow bags contain 4 striped teal bags, 1 vibrant maroon bag, 1 drab indigo bag, 4 muted beige bags.
faded indigo bags contain 2 posh lime bags, 1 vibrant teal bag.
posh tomato bags contain 4 striped salmon bags, 3 drab red bags.
light plum bags contain 3 bright blue bags, 5 dotted black bags, 4 shiny brown bags, 2 clear tan bags.
pale green bags contain 4 clear maroon bags, 4 dull green bags, 5 clear aqua bags, 3 drab beige bags.
drab brown bags contain 1 bright plum bag, 5 striped indigo bags, 1 vibrant lime bag.
muted lime bags contain 3 faded tan bags, 5 vibrant magenta bags, 5 posh coral bags.
faded violet bags contain 1 posh purple bag, 4 muted crimson bags, 5 striped red bags.
striped green bags contain 4 clear chartreuse bags, 4 dim maroon bags, 1 faded cyan bag, 5 faded silver bags.
dim plum bags contain 1 faded tan bag, 5 vibrant crimson bags, 3 light gray bags, 2 wavy teal bags.
drab cyan bags contain 4 muted plum bags, 5 mirrored black bags, 4 clear fuchsia bags.
vibrant lime bags contain 2 pale brown bags, 5 plaid violet bags.
drab purple bags contain 1 posh turquoise bag, 4 clear violet bags, 5 faded coral bags, 1 striped gold bag.
mirrored gray bags contain 3 dotted orange bags, 4 mirrored tomato bags, 4 plaid lime bags.
plaid teal bags contain 2 dim coral bags, 5 shiny magenta bags, 5 striped beige bags.
vibrant white bags contain 2 shiny red bags, 1 plaid black bag.
faded crimson bags contain 2 faded yellow bags.
dim chartreuse bags contain 4 mirrored teal bags, 5 light lavender bags.
wavy magenta bags contain 3 dark cyan bags.
mirrored magenta bags contain 4 muted salmon bags, 4 pale maroon bags.
plaid silver bags contain 2 pale turquoise bags, 3 posh salmon bags.
bright cyan bags contain 3 dark orange bags, 1 mirrored gold bag, 1 light violet bag, 5 faded silver bags.
faded orange bags contain 3 drab red bags, 5 dark tan bags, 2 vibrant magenta bags.
wavy gold bags contain 4 drab tomato bags, 2 muted yellow bags.
wavy salmon bags contain 2 dotted bronze bags, 3 light white bags, 2 dotted brown bags.
posh plum bags contain 4 drab black bags, 1 light silver bag.
dim aqua bags contain 5 striped black bags, 1 bright yellow bag, 4 posh salmon bags, 3 striped salmon bags.
shiny fuchsia bags contain 2 dim cyan bags.
dark tan bags contain 3 dull plum bags.
mirrored red bags contain 3 pale lime bags, 3 dim maroon bags.
bright purple bags contain 4 posh magenta bags, 4 wavy magenta bags, 3 posh plum bags, 3 dull lime bags.
striped olive bags contain 3 bright lavender bags, 3 mirrored black bags, 3 bright gold bags, 2 pale plum bags.
dotted bronze bags contain 3 dull coral bags, 1 faded black bag.
shiny green bags contain 1 shiny indigo bag.
mirrored chartreuse bags contain no other bags.
pale crimson bags contain 2 light orange bags, 3 light lime bags, 4 dotted cyan bags.
shiny lavender bags contain 5 shiny crimson bags, 5 striped tan bags.
wavy blue bags contain 1 pale brown bag, 2 light cyan bags, 1 light magenta bag, 4 pale tan bags.
muted plum bags contain 4 dull red bags, 1 dotted maroon bag, 1 vibrant red bag, 4 bright chartreuse bags.
vibrant violet bags contain 4 dull brown bags.
faded chartreuse bags contain 3 dotted yellow bags.
drab chartreuse bags contain 4 shiny gold bags.
posh crimson bags contain 3 clear cyan bags, 2 light crimson bags, 1 drab crimson bag, 5 clear blue bags.
drab tomato bags contain 4 striped salmon bags.
clear red bags contain 1 pale blue bag, 1 posh orange bag, 2 dark aqua bags, 5 posh red bags.
drab lavender bags contain 2 muted gray bags.
pale blue bags contain 5 pale beige bags, 3 muted green bags, 3 shiny white bags.
posh cyan bags contain 2 clear aqua bags, 2 drab chartreuse bags, 2 dark purple bags, 2 posh salmon bags.
faded silver bags contain 5 dim salmon bags, 2 striped bronze bags.
dim green bags contain 1 dark fuchsia bag.
plaid aqua bags contain 3 dim red bags, 3 drab turquoise bags, 3 dim aqua bags, 5 dull salmon bags.
posh fuchsia bags contain 2 dotted fuchsia bags.
striped lime bags contain 1 dull silver bag, 5 posh black bags, 1 dark fuchsia bag, 3 dull lime bags.
clear olive bags contain 1 pale crimson bag, 2 shiny orange bags, 2 posh magenta bags, 1 dark fuchsia bag.
bright lime bags contain 2 striped tan bags, 5 dull plum bags, 4 bright yellow bags.
faded green bags contain 2 pale turquoise bags, 5 light lime bags.
plaid indigo bags contain 1 drab crimson bag.
shiny turquoise bags contain 2 faded crimson bags.
drab aqua bags contain 4 mirrored red bags, 1 drab gold bag, 5 wavy orange bags.
dim gray bags contain 1 shiny lime bag, 5 dotted fuchsia bags.
light teal bags contain 5 pale beige bags, 4 shiny cyan bags, 2 striped red bags, 1 light orange bag.
wavy red bags contain 3 dotted tan bags, 3 pale aqua bags.
vibrant red bags contain no other bags.
striped salmon bags contain no other bags.
clear silver bags contain 1 shiny orange bag, 1 pale aqua bag, 1 faded purple bag, 2 dim coral bags.
muted tan bags contain 3 pale maroon bags, 4 dotted maroon bags, 2 bright plum bags, 4 pale teal bags.
faded yellow bags contain 2 striped black bags, 2 dotted chartreuse bags, 5 drab chartreuse bags, 5 shiny tomato bags.
dark green bags contain 1 light lime bag.
striped cyan bags contain 2 posh magenta bags, 2 dim cyan bags.
vibrant teal bags contain 2 dim magenta bags, 1 bright chartreuse bag, 5 bright tan bags, 1 bright yellow bag.
bright red bags contain 1 posh white bag.
bright magenta bags contain 3 posh salmon bags, 2 dull fuchsia bags, 1 posh lavender bag.
bright white bags contain 1 bright chartreuse bag, 1 mirrored yellow bag.
dotted teal bags contain 3 bright gray bags, 3 vibrant fuchsia bags.
clear blue bags contain 4 pale brown bags, 2 drab indigo bags, 2 pale salmon bags, 3 muted olive bags.
dull brown bags contain 1 dim cyan bag, 2 vibrant plum bags, 3 posh chartreuse bags.
vibrant tan bags contain 1 dark orange bag.
shiny white bags contain 3 mirrored violet bags, 1 drab indigo bag.
clear violet bags contain 2 vibrant crimson bags, 1 light gold bag, 2 striped silver bags.
bright coral bags contain 3 drab blue bags, 4 muted olive bags, 3 faded purple bags, 1 vibrant maroon bag.
dotted aqua bags contain 5 wavy black bags, 4 mirrored gold bags, 1 posh red bag, 2 plaid silver bags.
clear crimson bags contain 1 plaid gold bag.
faded fuchsia bags contain 5 shiny coral bags, 2 pale beige bags.
wavy crimson bags contain 4 dotted turquoise bags, 1 light gray bag, 5 wavy purple bags, 1 faded gray bag.
dark fuchsia bags contain 2 wavy brown bags, 3 vibrant orange bags.
striped plum bags contain 1 vibrant cyan bag, 3 posh lime bags.
shiny salmon bags contain 5 drab magenta bags, 4 mirrored turquoise bags.
dim brown bags contain 2 shiny gold bags, 5 dotted cyan bags, 3 plaid cyan bags.
posh violet bags contain 3 dim red bags, 2 posh white bags, 3 faded aqua bags, 4 shiny gold bags.
pale black bags contain 3 pale plum bags.
shiny red bags contain 4 posh salmon bags, 1 dotted chartreuse bag.
dull olive bags contain 2 light blue bags.
bright olive bags contain 2 striped olive bags, 3 muted plum bags, 2 striped magenta bags.
posh brown bags contain 1 vibrant gold bag, 2 wavy silver bags, 4 dotted salmon bags, 4 drab orange bags.
bright tan bags contain 3 light chartreuse bags.
dull beige bags contain 2 pale violet bags.
light yellow bags contain 2 clear indigo bags, 2 wavy brown bags, 2 bright black bags, 4 shiny lime bags.
dull aqua bags contain 2 dull black bags, 5 posh black bags, 2 wavy fuchsia bags.
dark gold bags contain 3 clear fuchsia bags, 1 dark cyan bag, 4 dark orange bags.
wavy white bags contain 2 dark brown bags, 5 drab yellow bags, 5 dotted turquoise bags, 4 muted tomato bags.
posh silver bags contain 2 dim chartreuse bags, 5 light fuchsia bags, 4 faded purple bags, 5 drab cyan bags.
dotted coral bags contain 5 plaid silver bags, 2 posh beige bags, 5 dim beige bags, 2 vibrant crimson bags.
drab silver bags contain 1 posh chartreuse bag.
dull teal bags contain 1 dim indigo bag.
wavy brown bags contain no other bags.
posh purple bags contain 1 wavy purple bag, 5 muted gold bags.
faded magenta bags contain 2 wavy aqua bags, 4 vibrant beige bags.
vibrant magenta bags contain 5 wavy black bags, 4 shiny maroon bags, 3 dim tomato bags, 5 vibrant gray bags.
mirrored brown bags contain 2 light aqua bags, 1 clear orange bag, 2 bright lavender bags.
light crimson bags contain 5 posh chartreuse bags.
dotted olive bags contain 5 dim tomato bags, 3 dim plum bags.
light indigo bags contain 1 bright gold bag, 4 drab chartreuse bags, 4 dim fuchsia bags, 3 vibrant black bags.
vibrant chartreuse bags contain 5 dim crimson bags, 1 clear plum bag, 4 striped black bags.
pale violet bags contain 3 dark salmon bags.
bright violet bags contain 3 striped aqua bags.
dull maroon bags contain 1 drab aqua bag, 3 mirrored lavender bags, 5 dotted brown bags.
dim lime bags contain 3 wavy salmon bags, 3 striped tan bags.
dotted tan bags contain 3 dull yellow bags, 3 shiny violet bags.
posh yellow bags contain 3 dull crimson bags, 4 dim olive bags, 4 dark black bags.
dull violet bags contain 4 bright yellow bags, 2 posh magenta bags, 5 shiny red bags.
dotted silver bags contain 2 wavy turquoise bags, 3 dull tomato bags, 3 bright tan bags, 1 dotted salmon bag.
pale gray bags contain 1 plaid turquoise bag, 4 bright salmon bags.
clear purple bags contain 5 shiny gold bags, 5 faded teal bags.
striped tan bags contain 1 mirrored cyan bag, 2 pale beige bags.
dotted indigo bags contain 2 pale purple bags, 2 pale black bags, 2 dark salmon bags.
clear turquoise bags contain 2 light lavender bags.
wavy plum bags contain 5 shiny aqua bags.
muted indigo bags contain 5 drab teal bags.
muted yellow bags contain 2 vibrant cyan bags, 1 dim white bag.
dark white bags contain 2 drab crimson bags, 5 dull gray bags.
faded blue bags contain 1 faded olive bag, 2 shiny magenta bags, 5 dark plum bags.
posh tan bags contain 2 posh plum bags, 5 muted black bags, 3 clear indigo bags, 4 striped gold bags.
striped silver bags contain 4 drab tomato bags.
muted lavender bags contain 3 dim silver bags, 2 wavy lavender bags, 1 faded tan bag.
wavy chartreuse bags contain 5 dull bronze bags.
dark blue bags contain 1 dotted silver bag, 3 light yellow bags, 3 mirrored bronze bags, 4 shiny lavender bags.
dim turquoise bags contain 3 pale green bags, 4 mirrored gray bags.
muted blue bags contain 1 striped lavender bag, 3 dark fuchsia bags.
faded brown bags contain 2 dotted violet bags, 5 faded indigo bags, 5 drab indigo bags.
shiny magenta bags contain 5 dotted turquoise bags, 3 plaid violet bags, 2 dim cyan bags.
clear chartreuse bags contain 3 pale maroon bags, 5 plaid blue bags, 1 clear tan bag.
faded turquoise bags contain 4 mirrored magenta bags.
posh turquoise bags contain 3 dotted yellow bags, 5 striped purple bags, 3 pale cyan bags.
vibrant tomato bags contain 4 dark cyan bags.
mirrored white bags contain 2 mirrored indigo bags, 3 dim cyan bags, 3 bright lavender bags.
dull purple bags contain 2 striped yellow bags, 3 dull plum bags, 3 shiny gold bags, 3 pale gold bags.
mirrored yellow bags contain 4 shiny crimson bags.
posh white bags contain 3 mirrored orange bags.
wavy fuchsia bags contain 3 dotted tan bags, 5 shiny coral bags.
mirrored green bags contain 1 dull white bag, 5 shiny crimson bags.
plaid turquoise bags contain 2 pale salmon bags, 4 dull beige bags.
clear cyan bags contain 1 dim silver bag, 4 drab chartreuse bags.
mirrored purple bags contain 1 dull coral bag, 3 vibrant plum bags.
dim lavender bags contain 1 striped black bag, 4 shiny red bags, 4 posh chartreuse bags, 2 dim teal bags.
plaid cyan bags contain 1 dim orange bag.
plaid magenta bags contain 5 striped red bags, 4 striped salmon bags.
shiny blue bags contain 2 shiny turquoise bags, 1 posh orange bag.
faded aqua bags contain 3 light yellow bags, 3 wavy purple bags, 5 dull lime bags, 5 dotted black bags.
mirrored blue bags contain 5 wavy silver bags.
posh indigo bags contain 5 dark tan bags, 2 vibrant blue bags, 5 dark bronze bags, 2 vibrant crimson bags.
clear plum bags contain 1 wavy teal bag, 1 faded yellow bag.
dark gray bags contain 4 bright lavender bags.
muted coral bags contain 4 shiny red bags, 2 pale teal bags, 4 dim olive bags, 3 muted silver bags.
dim gold bags contain 2 pale gold bags, 3 vibrant red bags.
plaid violet bags contain 3 faded green bags, 4 mirrored teal bags, 1 wavy purple bag, 1 faded yellow bag.
clear tomato bags contain 2 drab beige bags, 3 dim cyan bags.
bright beige bags contain 5 muted brown bags, 4 wavy red bags, 4 clear maroon bags.
wavy teal bags contain 4 muted beige bags, 1 posh salmon bag, 2 posh black bags, 2 dotted maroon bags.
vibrant salmon bags contain 4 vibrant purple bags, 4 dull chartreuse bags.
dull coral bags contain 2 light red bags, 3 dark plum bags, 3 bright gray bags, 1 dotted cyan bag.
bright turquoise bags contain 4 plaid teal bags, 3 muted orange bags.
wavy maroon bags contain 5 pale fuchsia bags, 5 dotted magenta bags.
plaid gold bags contain 2 shiny lavender bags, 1 vibrant gray bag, 5 mirrored teal bags.
wavy black bags contain 1 wavy magenta bag.
drab beige bags contain 1 mirrored chartreuse bag, 3 wavy brown bags, 4 pale beige bags, 2 pale turquoise bags.
posh blue bags contain 4 clear silver bags.
vibrant turquoise bags contain 1 posh white bag, 2 bright gold bags.
faded black bags contain 5 wavy black bags, 1 shiny crimson bag.
pale salmon bags contain 1 vibrant brown bag.
striped gray bags contain 1 mirrored violet bag, 4 dull violet bags, 4 muted turquoise bags.
light brown bags contain 5 muted crimson bags, 1 drab crimson bag, 4 muted aqua bags, 5 dotted blue bags.
striped turquoise bags contain 5 muted blue bags, 4 mirrored salmon bags.
shiny lime bags contain 1 vibrant purple bag, 4 pale turquoise bags, 4 drab tomato bags, 4 dotted maroon bags.
dotted white bags contain 5 pale violet bags, 1 posh plum bag, 1 shiny chartreuse bag, 2 faded bronze bags.
dotted crimson bags contain 2 shiny olive bags, 2 mirrored yellow bags.
mirrored teal bags contain 1 dull violet bag, 4 shiny red bags, 3 drab black bags, 1 posh magenta bag.
striped lavender bags contain 4 light crimson bags.
pale chartreuse bags contain 1 wavy red bag.
posh gray bags contain 3 posh black bags.
clear teal bags contain 4 dull violet bags, 4 dotted chartreuse bags, 3 drab tan bags.
light olive bags contain 3 muted olive bags, 4 plaid turquoise bags.
light tomato bags contain 5 dull chartreuse bags, 3 muted beige bags.
light orange bags contain 2 wavy lavender bags.
wavy coral bags contain 5 drab beige bags, 4 plaid white bags.
dotted violet bags contain 5 muted salmon bags, 5 shiny red bags, 3 shiny crimson bags.
muted fuchsia bags contain 5 dull coral bags.
pale turquoise bags contain 3 vibrant red bags.
faded beige bags contain 2 striped magenta bags.
dull tan bags contain 3 drab maroon bags, 3 muted beige bags.
posh lime bags contain 4 wavy turquoise bags, 2 light blue bags, 1 posh salmon bag.
drab magenta bags contain 5 dim magenta bags.
striped crimson bags contain 1 dull white bag, 4 muted plum bags, 1 posh chartreuse bag.
vibrant maroon bags contain 4 pale aqua bags.
dotted black bags contain 5 shiny bronze bags, 1 shiny lime bag, 5 dotted yellow bags, 1 wavy turquoise bag.
wavy aqua bags contain 3 dull tomato bags, 1 shiny olive bag, 4 vibrant brown bags, 2 dim chartreuse bags.
dim tan bags contain 2 bright plum bags, 4 striped gold bags, 4 dull coral bags.
dull fuchsia bags contain 5 wavy maroon bags.
striped red bags contain 5 shiny red bags, 4 clear gold bags, 4 posh magenta bags, 2 bright yellow bags.
dotted lavender bags contain 3 faded lavender bags.
muted turquoise bags contain 4 faded fuchsia bags.
bright gray bags contain 2 light silver bags, 3 dull violet bags.
dull indigo bags contain 2 dim violet bags, 3 plaid salmon bags, 5 plaid beige bags.
wavy purple bags contain 3 dim yellow bags, 1 posh salmon bag.
wavy lime bags contain 2 dark fuchsia bags, 3 dark salmon bags, 5 bright silver bags, 5 pale aqua bags.
light cyan bags contain 2 clear blue bags.
light beige bags contain 5 dull red bags, 3 dark violet bags, 5 shiny lime bags.
mirrored silver bags contain 1 plaid beige bag, 5 dull coral bags.
dark beige bags contain 1 clear tan bag, 4 wavy orange bags, 3 shiny cyan bags, 5 shiny magenta bags.
vibrant crimson bags contain 2 mirrored teal bags, 3 pale turquoise bags, 5 posh magenta bags.
faded red bags contain 3 plaid lime bags, 2 clear brown bags.
dim bronze bags contain 2 dark beige bags, 1 plaid cyan bag, 3 clear purple bags.
bright maroon bags contain 3 light gray bags, 2 faded turquoise bags, 1 posh cyan bag.
clear gray bags contain 4 faded green bags.
pale silver bags contain 3 dull magenta bags.
dotted red bags contain 2 clear purple bags, 1 faded crimson bag, 5 dull bronze bags, 5 muted plum bags.
striped maroon bags contain 5 mirrored cyan bags, 3 dark green bags, 4 clear indigo bags, 2 muted beige bags.
dark cyan bags contain 3 dotted maroon bags, 2 vibrant red bags.
clear bronze bags contain 1 drab lime bag, 5 light gold bags.
dull yellow bags contain 1 dull chartreuse bag, 1 muted olive bag.
plaid lavender bags contain 1 vibrant silver bag, 5 clear fuchsia bags.
posh black bags contain 5 dotted salmon bags, 4 drab tomato bags, 5 drab black bags.
faded lime bags contain 1 dark silver bag.
clear lavender bags contain 5 light violet bags.
dotted gray bags contain 4 clear lavender bags, 3 shiny magenta bags.
shiny gray bags contain 5 dull brown bags.
drab coral bags contain 2 faded beige bags.
dark teal bags contain 3 drab indigo bags, 2 light aqua bags, 1 faded tan bag, 2 wavy brown bags.
shiny violet bags contain 1 posh black bag, 5 dim beige bags.
clear salmon bags contain 5 clear orange bags.
shiny olive bags contain 2 shiny yellow bags, 1 shiny indigo bag, 4 bright yellow bags.
plaid salmon bags contain 4 striped yellow bags, 4 mirrored chartreuse bags, 3 light magenta bags, 2 mirrored magenta bags.
wavy orange bags contain 5 vibrant purple bags.
posh magenta bags contain 3 mirrored chartreuse bags, 4 vibrant red bags.
pale fuchsia bags contain 5 muted silver bags.
light black bags contain 5 wavy orange bags, 5 faded tomato bags.
light gold bags contain 1 dull red bag.
bright brown bags contain 5 mirrored beige bags, 5 faded indigo bags.
muted teal bags contain 5 posh magenta bags, 1 dim gray bag, 3 pale plum bags.
pale plum bags contain 2 muted beige bags, 2 posh magenta bags, 2 shiny gold bags.
drab gold bags contain 1 striped beige bag.
posh gold bags contain 3 shiny silver bags.
dull turquoise bags contain 4 vibrant crimson bags, 3 faded gray bags, 5 muted purple bags.
light chartreuse bags contain 2 bright lavender bags, 4 bright silver bags.
striped chartreuse bags contain 1 shiny coral bag, 2 clear blue bags, 2 dotted turquoise bags.
dark aqua bags contain 3 wavy bronze bags, 4 shiny brown bags, 2 bright violet bags, 1 dotted indigo bag.
muted bronze bags contain 3 pale salmon bags, 1 striped teal bag.
dark violet bags contain 2 wavy magenta bags.
dark maroon bags contain 2 muted red bags.
shiny silver bags contain 2 light gray bags, 1 pale aqua bag, 5 dim tomato bags.
bright lavender bags contain 5 striped red bags, 3 faded tan bags.
dim olive bags contain 3 posh cyan bags, 4 light aqua bags, 1 wavy tan bag, 3 dull silver bags.
posh beige bags contain 5 faded tan bags, 1 shiny lime bag, 4 wavy lavender bags.
muted maroon bags contain 3 mirrored purple bags, 2 mirrored gold bags, 1 clear tan bag.
vibrant yellow bags contain 4 light lavender bags.
light purple bags contain 1 faded olive bag, 1 wavy red bag.
bright yellow bags contain 3 dotted salmon bags, 4 posh magenta bags, 4 striped salmon bags.
dull gray bags contain 5 posh magenta bags, 1 shiny white bag, 2 dim bronze bags, 2 dim lavender bags.
vibrant plum bags contain 1 faded tan bag, 2 pale turquoise bags, 4 bright chartreuse bags, 4 dull violet bags.
posh chartreuse bags contain 1 bright chartreuse bag, 4 drab black bags, 2 posh magenta bags, 4 dark orange bags.
drab gray bags contain 4 plaid turquoise bags.
dark brown bags contain 4 dotted green bags, 3 dim lavender bags.
mirrored crimson bags contain 2 light teal bags, 2 plaid blue bags, 5 wavy red bags, 2 bright tomato bags.
dotted gold bags contain 4 bright olive bags.
dark salmon bags contain 3 pale turquoise bags, 5 faded tan bags, 1 mirrored chartreuse bag.
wavy gray bags contain 4 shiny green bags, 5 shiny red bags.
dotted blue bags contain 2 wavy yellow bags, 1 dull beige bag.
dim maroon bags contain 2 wavy maroon bags, 5 dim violet bags, 4 dark tan bags.
plaid purple bags contain 2 dark teal bags, 2 mirrored black bags, 1 wavy lavender bag.
dull blue bags contain 1 bright gold bag, 2 dim olive bags, 4 muted chartreuse bags, 2 striped salmon bags.
muted white bags contain 4 light bronze bags, 3 wavy beige bags.
muted gold bags contain no other bags.
drab green bags contain 2 plaid chartreuse bags.
clear coral bags contain 5 mirrored cyan bags.
drab turquoise bags contain 3 posh black bags.
dotted fuchsia bags contain 2 light red bags, 4 clear aqua bags, 1 posh magenta bag, 4 vibrant cyan bags.
clear lime bags contain 3 dark chartreuse bags.
mirrored plum bags contain 1 wavy tan bag, 2 bright olive bags.
vibrant coral bags contain 3 light gray bags, 5 light white bags.
pale bronze bags contain 2 bright silver bags, 5 vibrant tan bags, 4 posh lime bags, 3 wavy silver bags.
plaid blue bags contain 4 dotted beige bags, 2 wavy olive bags, 2 striped tomato bags.
shiny teal bags contain 2 shiny violet bags, 1 faded blue bag, 5 shiny white bags, 4 dim fuchsia bags.
clear black bags contain 4 faded purple bags, 1 dim tomato bag, 5 striped brown bags, 2 faded indigo bags.
clear orange bags contain 2 bright gold bags, 5 light crimson bags, 2 faded yellow bags.
drab maroon bags contain 1 vibrant red bag, 2 dotted bronze bags.
drab blue bags contain 1 mirrored aqua bag, 1 dark gold bag, 3 shiny crimson bags.
striped black bags contain 2 drab black bags, 5 dark orange bags.
light lavender bags contain 1 clear blue bag, 1 striped red bag.
posh bronze bags contain 5 light red bags, 4 dull plum bags, 1 dim coral bag, 3 clear blue bags.
plaid beige bags contain 5 dotted turquoise bags, 2 light cyan bags.
plaid fuchsia bags contain 3 wavy fuchsia bags.
shiny bronze bags contain 5 vibrant silver bags, 3 striped silver bags, 3 pale turquoise bags, 2 faded olive bags.
vibrant purple bags contain 3 wavy magenta bags.
pale magenta bags contain 4 dim yellow bags, 1 dim aqua bag.
faded purple bags contain 5 mirrored black bags, 1 muted beige bag, 1 muted aqua bag, 1 light maroon bag.
light turquoise bags contain 5 muted brown bags, 1 posh beige bag, 2 vibrant fuchsia bags, 3 faded teal bags.
vibrant lavender bags contain 1 light chartreuse bag, 3 mirrored teal bags, 5 drab lavender bags, 4 shiny brown bags.
striped yellow bags contain 1 dotted cyan bag, 3 mirrored turquoise bags.
drab bronze bags contain 3 shiny lavender bags, 5 muted yellow bags, 3 plaid teal bags, 2 plaid gold bags.
posh maroon bags contain 5 bright fuchsia bags, 3 dotted indigo bags, 5 dark teal bags, 1 faded violet bag.
vibrant cyan bags contain 2 dark orange bags.
striped aqua bags contain 2 light bronze bags, 1 dull beige bag, 4 pale violet bags, 5 pale beige bags.
faded gold bags contain 4 pale crimson bags.
muted olive bags contain 2 mirrored teal bags, 1 dim aqua bag, 3 posh chartreuse bags, 3 dull brown bags.
dim coral bags contain 1 mirrored gold bag.
dull silver bags contain 5 faded gray bags, 5 light red bags, 3 light crimson bags, 4 bright chartreuse bags.
vibrant gray bags contain 2 plaid silver bags, 5 plaid violet bags, 1 dim silver bag, 4 mirrored chartreuse bags.
plaid crimson bags contain 2 vibrant bronze bags, 1 drab olive bag, 1 pale purple bag.
dotted maroon bags contain no other bags.
vibrant brown bags contain 2 dull violet bags, 4 muted beige bags, 4 wavy teal bags.
bright tomato bags contain 3 muted beige bags.
shiny cyan bags contain 5 clear gold bags, 2 shiny lime bags, 4 wavy magenta bags, 2 wavy lavender bags.
drab tan bags contain 1 plaid red bag.
dull plum bags contain 4 dotted magenta bags, 1 plaid silver bag, 1 pale teal bag, 1 dim yellow bag.
clear gold bags contain 1 bright gold bag, 4 dark orange bags, 4 posh magenta bags.
shiny gold bags contain 5 dark salmon bags, 2 wavy purple bags, 5 dark cyan bags, 5 dull chartreuse bags.
mirrored tomato bags contain 3 light aqua bags, 4 pale plum bags, 1 pale beige bag.
dim tomato bags contain 5 light crimson bags, 2 bright lavender bags.
mirrored tan bags contain 1 vibrant plum bag, 2 faded violet bags, 5 striped lime bags, 3 muted white bags.
faded teal bags contain 1 drab silver bag.
dim red bags contain 2 clear turquoise bags, 3 drab maroon bags.
dark magenta bags contain 2 clear cyan bags.
vibrant gold bags contain 4 dotted salmon bags, 3 bright chartreuse bags, 3 striped purple bags.
muted brown bags contain 4 posh beige bags, 3 muted aqua bags, 5 dim beige bags, 4 dim magenta bags.
plaid orange bags contain 2 dark purple bags, 4 mirrored tomato bags, 1 vibrant orange bag.
pale gold bags contain 1 vibrant plum bag, 4 dotted violet bags.
plaid gray bags contain 3 bright silver bags, 5 drab fuchsia bags.
muted orange bags contain 5 dull magenta bags, 5 clear lavender bags, 4 mirrored chartreuse bags, 4 vibrant silver bags.
muted aqua bags contain 2 dim silver bags, 2 wavy black bags.
dim crimson bags contain 2 mirrored bronze bags, 4 muted cyan bags.
dark tomato bags contain 5 pale blue bags.
bright salmon bags contain 1 vibrant tan bag, 4 bright white bags, 1 dim gray bag.
mirrored orange bags contain 1 dark salmon bag, 5 drab beige bags, 5 dull chartreuse bags, 1 shiny cyan bag.
clear aqua bags contain 2 dim teal bags, 4 wavy olive bags.
bright bronze bags contain 3 shiny maroon bags.
vibrant black bags contain 3 muted gold bags, 2 striped red bags, 2 pale magenta bags, 4 clear violet bags.
clear yellow bags contain 2 plaid maroon bags.
pale lavender bags contain 1 shiny maroon bag, 5 bright cyan bags, 5 shiny orange bags, 4 striped tomato bags.
dark chartreuse bags contain 2 wavy brown bags.
mirrored violet bags contain 2 light lavender bags, 4 dull coral bags, 2 light red bags.
vibrant beige bags contain 2 shiny red bags, 2 clear tan bags.
mirrored coral bags contain 4 faded coral bags, 2 dull bronze bags.
posh red bags contain 4 wavy brown bags, 1 dark salmon bag, 5 dull chartreuse bags, 5 vibrant crimson bags.
light green bags contain 4 posh fuchsia bags.
wavy green bags contain 3 dark green bags, 4 posh chartreuse bags, 1 mirrored black bag.
drab violet bags contain 5 wavy yellow bags.
dark crimson bags contain 1 bright gray bag, 2 shiny violet bags, 3 pale chartreuse bags.
posh green bags contain 2 bright yellow bags, 2 faded yellow bags.
shiny plum bags contain 3 shiny indigo bags, 1 dark gold bag, 2 dim coral bags.
striped beige bags contain 2 muted beige bags.
dark orange bags contain 5 bright gold bags, 2 dotted maroon bags, 1 striped salmon bag, 3 vibrant red bags.
bright orange bags contain 4 muted blue bags, 5 striped blue bags, 4 dark cyan bags.
dark black bags contain 1 shiny lime bag, 1 clear olive bag, 4 dull bronze bags, 3 muted lavender bags.
pale orange bags contain 3 plaid violet bags, 1 shiny red bag, 1 dull coral bag, 1 shiny bronze bag.
mirrored salmon bags contain 4 vibrant red bags, 3 muted beige bags, 2 dark orange bags.
drab yellow bags contain 1 bright white bag.
dull tomato bags contain 4 muted beige bags, 3 posh salmon bags, 2 shiny maroon bags.
striped fuchsia bags contain 5 pale beige bags, 3 mirrored gray bags.
mirrored beige bags contain 5 mirrored black bags, 2 dim lavender bags, 1 clear lime bag.
wavy tomato bags contain 4 wavy fuchsia bags.
bright indigo bags contain 2 dull violet bags, 5 dull green bags, 3 dotted cyan bags, 2 dotted tan bags.
striped blue bags contain 1 posh red bag, 4 bright fuchsia bags, 4 dark aqua bags.
bright green bags contain 3 dim violet bags, 2 shiny coral bags, 1 dim white bag, 4 dim yellow bags.
dotted salmon bags contain 5 dull red bags, 2 striped salmon bags, 5 dotted maroon bags, 3 shiny red bags.
light magenta bags contain 1 dark fuchsia bag, 1 pale turquoise bag, 5 pale plum bags, 3 vibrant tan bags.
mirrored olive bags contain 1 shiny lavender bag.
dark coral bags contain 3 wavy teal bags, 4 muted plum bags.
posh teal bags contain 1 pale violet bag, 5 muted tan bags, 1 drab gray bag, 2 drab beige bags.
bright teal bags contain 5 mirrored coral bags.
striped orange bags contain 3 clear olive bags.
faded plum bags contain 5 striped black bags, 1 striped gold bag.
plaid tomato bags contain 1 muted salmon bag, 2 pale violet bags, 1 light violet bag, 3 dim tomato bags.
dim blue bags contain 4 drab salmon bags, 4 faded plum bags, 1 light salmon bag, 3 dark turquoise bags.
striped coral bags contain 3 wavy fuchsia bags.
light violet bags contain 4 dim beige bags, 4 striped lavender bags, 1 dotted orange bag, 1 wavy purple bag.
dull white bags contain 2 faded purple bags, 1 bright silver bag, 4 pale bronze bags, 3 clear fuchsia bags.
dim white bags contain 2 light yellow bags, 5 posh gold bags, 1 bright blue bag, 1 striped chartreuse bag.
bright chartreuse bags contain 1 muted gold bag, 1 dotted maroon bag.
striped purple bags contain 2 light orange bags, 1 dotted maroon bag, 3 dim magenta bags, 4 plaid violet bags.
dotted tomato bags contain 5 posh chartreuse bags.
wavy lavender bags contain 4 dim yellow bags, 4 pale turquoise bags, 4 vibrant red bags, 3 bright yellow bags.
striped teal bags contain 2 bright yellow bags.
drab crimson bags contain 1 wavy tan bag, 1 dull green bag, 3 muted blue bags.
dull lime bags contain 3 shiny tomato bags.
posh salmon bags contain no other bags.
vibrant aqua bags contain 2 shiny indigo bags, 3 shiny crimson bags, 4 shiny cyan bags.
drab black bags contain 3 dull violet bags, 4 dotted maroon bags, 3 vibrant purple bags, 3 muted plum bags.
drab olive bags contain 5 drab orange bags, 4 dotted green bags, 5 drab chartreuse bags.
dark plum bags contain 2 dotted salmon bags, 5 wavy magenta bags, 1 bright chartreuse bag.
plaid brown bags contain 2 light lavender bags.
striped magenta bags contain 5 pale lime bags, 4 posh salmon bags, 5 clear tomato bags, 5 dull plum bags.
dull orange bags contain 4 light maroon bags.
vibrant orange bags contain 5 dull red bags, 1 posh chartreuse bag.
mirrored turquoise bags contain 4 drab cyan bags, 1 posh cyan bag, 4 clear gold bags, 5 plaid magenta bags.
mirrored black bags contain no other bags.
shiny black bags contain 5 dotted green bags, 1 dim violet bag, 1 clear cyan bag, 2 muted fuchsia bags.
vibrant indigo bags contain 1 light maroon bag.
bright fuchsia bags contain 5 faded olive bags.
dotted plum bags contain 5 shiny violet bags.
plaid lime bags contain 2 bright gray bags, 4 pale beige bags, 4 light silver bags.
plaid red bags contain 1 shiny maroon bag, 4 striped lavender bags, 5 mirrored purple bags.
mirrored lime bags contain 5 faded coral bags, 3 dark gold bags, 5 mirrored indigo bags, 5 dull coral bags.
drab lime bags contain 2 dotted aqua bags, 5 shiny chartreuse bags.
faded tan bags contain 1 muted plum bag, 1 posh salmon bag.
dark silver bags contain 4 dotted maroon bags, 4 shiny white bags.
striped indigo bags contain 5 dull plum bags, 2 light lavender bags, 3 light red bags, 1 muted olive bag.
bright gold bags contain no other bags.
plaid black bags contain 2 dull violet bags, 5 muted olive bags, 1 muted teal bag.
dotted chartreuse bags contain no other bags.
vibrant blue bags contain 1 shiny cyan bag.
dim indigo bags contain 1 bright purple bag, 1 plaid magenta bag, 5 posh fuchsia bags, 5 plaid red bags.
light red bags contain 5 bright gold bags, 4 plaid silver bags, 1 dull violet bag, 4 pale turquoise bags.
dim black bags contain 3 dim orange bags, 5 dull lime bags, 2 faded indigo bags, 3 dotted olive bags.
mirrored gold bags contain 2 muted gold bags, 5 dark cyan bags.
posh aqua bags contain 1 clear violet bag.
light blue bags contain 3 drab chartreuse bags, 2 dull chartreuse bags.
shiny maroon bags contain 1 wavy violet bag.
faded lavender bags contain 1 dark salmon bag, 5 vibrant orange bags, 3 vibrant purple bags, 5 posh black bags.
faded olive bags contain 2 mirrored teal bags, 5 pale plum bags, 4 pale brown bags.
drab indigo bags contain 1 dim cyan bag, 1 plaid silver bag.
clear white bags contain 4 posh beige bags.
wavy violet bags contain 5 dotted fuchsia bags.
dark turquoise bags contain 5 vibrant turquoise bags, 3 vibrant lavender bags.
striped violet bags contain 5 mirrored turquoise bags, 1 muted orange bag, 3 dim teal bags, 4 posh green bags.
wavy yellow bags contain 2 dim yellow bags, 5 dim lavender bags.
dark red bags contain 4 striped gold bags, 3 vibrant tomato bags.
plaid maroon bags contain 5 light white bags, 5 plaid black bags.
bright black bags contain 3 light maroon bags, 5 shiny lime bags, 2 vibrant maroon bags, 3 clear violet bags.
drab salmon bags contain 2 clear coral bags, 4 dark indigo bags.
plaid green bags contain 2 pale indigo bags.
pale teal bags contain 4 drab black bags, 3 faded gray bags, 5 posh beige bags, 4 faded yellow bags.
light silver bags contain 5 bright yellow bags, 1 dim silver bag, 5 posh chartreuse bags.
dull magenta bags contain 3 posh turquoise bags, 3 light magenta bags, 4 shiny orange bags, 4 clear turquoise bags.
pale white bags contain 5 dark cyan bags.
dull chartreuse bags contain 3 mirrored black bags, 3 dotted salmon bags, 5 pale turquoise bags.
dim salmon bags contain 2 mirrored yellow bags, 5 striped salmon bags, 1 drab tomato bag, 5 dull yellow bags.
shiny crimson bags contain 5 faded tan bags, 2 muted salmon bags, 1 wavy teal bag, 3 vibrant orange bags.
dark purple bags contain 2 muted plum bags, 5 bright lavender bags, 1 dark cyan bag, 4 clear orange bags.
clear brown bags contain 2 dim orange bags, 1 vibrant maroon bag, 2 striped lime bags.
muted silver bags contain 5 vibrant gray bags.
vibrant bronze bags contain 3 posh red bags.
mirrored maroon bags contain 3 clear magenta bags, 2 posh brown bags, 5 wavy teal bags.
muted tomato bags contain 5 faded aqua bags, 4 wavy lavender bags, 1 mirrored silver bag.
posh olive bags contain 4 faded salmon bags, 1 muted green bag, 5 light tomato bags, 3 dark gold bags.
dotted turquoise bags contain 5 light orange bags, 1 dull brown bag.
light bronze bags contain 2 pale cyan bags, 3 shiny lime bags, 2 faded olive bags.
striped gold bags contain 4 muted salmon bags, 1 bright yellow bag, 1 dark plum bag, 4 light maroon bags.
faded maroon bags contain 5 wavy silver bags, 3 plaid magenta bags.
clear magenta bags contain 2 wavy turquoise bags.
vibrant olive bags contain 1 muted silver bag.
clear tan bags contain 4 mirrored gold bags.
posh orange bags contain 3 plaid blue bags, 4 dotted aqua bags.
wavy cyan bags contain 3 posh lavender bags.
shiny chartreuse bags contain 5 mirrored cyan bags, 3 posh chartreuse bags, 4 dotted aqua bags.
light lime bags contain 5 muted plum bags, 2 wavy purple bags.
wavy silver bags contain 4 faded lavender bags.
drab red bags contain 4 clear tomato bags, 4 pale turquoise bags, 2 dull yellow bags.
light aqua bags contain 3 dotted aqua bags.
dim purple bags contain 2 striped gold bags, 2 drab tan bags, 2 mirrored tan bags.
shiny indigo bags contain 1 pale magenta bag, 5 dim plum bags, 3 muted blue bags, 4 dim coral bags.
pale lime bags contain 2 mirrored cyan bags, 4 dull violet bags, 1 striped lime bag.
posh lavender bags contain 5 clear purple bags, 2 muted gold bags, 5 dull brown bags, 4 muted lime bags.
dull lavender bags contain 1 striped violet bag, 3 muted bronze bags.
dotted lime bags contain 3 plaid magenta bags, 5 plaid violet bags, 1 shiny lime bag, 3 plaid purple bags.
posh coral bags contain 5 mirrored violet bags, 1 clear violet bag, 1 dark fuchsia bag, 3 dotted silver bags.
bright plum bags contain 5 wavy brown bags.
pale coral bags contain 3 bright olive bags.
dim fuchsia bags contain 2 bright chartreuse bags, 4 mirrored teal bags, 4 posh salmon bags, 3 light chartreuse bags.
dim cyan bags contain 2 faded tan bags, 4 mirrored gold bags.
faded cyan bags contain 1 dotted black bag, 1 shiny maroon bag, 2 muted chartreuse bags."""
