from colorama import init, Fore, Style
init(convert=True)

specialChars = {
    "perpendicular": "⟂",
    "triangle": "△",
    "angle": "∠",
    "parallel": "//",
    "side": "",
}


def generatePrintHeader(mainStr, restStr,
                        mainColor=Fore.GREEN, restColor=Fore.CYAN):
    '''Generate header with color'''
    strWithStyle = mainColor + mainStr + " " \
        + restColor + restStr       \
        + Style.RESET_ALL
    return "Generating {} snippet...".format(strWithStyle)


def getCaseInput(cases):
    print("Available case: ")
    for index, case in enumerate(cases):
        print("\t{}. {}".format(index, case['caseName']))
    return int(input("Your case: "))


def getCongruentText(firstEle, secondEle, reason):
    if reason:
        # Not empty
        reason = "({})".format(reason)

    if firstEle == secondEle:
        return "\t{} is common\t{}\n".format(
            firstEle,
            reason
        )
    else:
        return "\t{} = {}\t{}\n".format(
            firstEle,
            secondEle,
            reason
        )


def promptCongruentPair(pairNumber, pairType):
    '''Prompt user for congruent pair'''
    pairText = ""
    if pairNumber != 0:
        pairText = "Pair {}, ".format(pairNumber)

    ele1 = specialChars[pairType] + \
        input("\t{}{} 1: ".format(pairText, pairType))
    ele2 = specialChars[pairType] + \
        input("\t{}{} 2: ".format(pairText, pairType))
    reason = input("\t  Reason for congruent: ")

    return getCongruentText(ele1, ele2, reason)


def handlePrompt(availCases, type):
    '''In charge of getting inputs from user'''
    caseIndex = getCaseInput(availCases)
    if caseIndex < 0 or caseIndex > len(availCases):
        return "{}Invalid{} case! Exiting...".format(Fore.RED, Style.RESET_ALL)

    case = availCases[caseIndex]
    caseName = case['caseName']
    print("Generating input for case: {}".format(
        Fore.GREEN + caseName + Style.RESET_ALL))

    print("If anything is common, please type the same name for each side")
    print("Please input the names of: ")
    firstName = input("\tFirst triangle: ")
    secondName = input("\tSecond triangle: ")
    result = "Let's consider {} and {}, we have:\n".format(
        specialChars["triangle"] + firstName,
        specialChars["triangle"] + secondName)

    for i in range(len(case['pairOrderData'])):
        result += promptCongruentPair(case['pairOrderData'][i],
                                      case['pairNameData'][i])

    result += "Therefore, the 2 triangles are {} ({})".format(
        type, caseName)
    return result


def generateCTPS():
    '''Generate snippets for Congruent triangle pair snippet'''
    print(generatePrintHeader("Congruent", "triangle pair"))

    availCases = [
        {
            "caseName": "ASA",
            "pairOrderData": [1, 0, 2],
            "pairNameData": ["angle", "side", "angle"],
        },
        {
            "caseName": "SAS",
            "pairOrderData": [1, 0, 2],
            "pairNameData": ["side", "angle", "side"],
        },
        {
            "caseName": "SSS",
            "pairOrderData": [1, 2, 3],
            "pairNameData": ["side", "side", "side"],
        },
        {
            "caseName": "AAS",
            "pairOrderData": [1, 2, 0],
            "pairNameData": ["angle", "angle", "side"],
        }]
    return handlePrompt(availCases, "congruent")


def generateSTPS():
    '''Generate snippets for Similar triangle pair snippet'''
    print(generatePrintHeader("Similar", "triangle pair"))

    availCases = [
        {
            "caseName": "SAS",
            "pairOrderData": [1, 0, 2],
            "pairNameData": ["side", "angle", "side"],
        },
        {
            "caseName": "SSS",
            "pairOrderData": [1, 2, 3],
            "pairNameData": ["side", "side", "side"],
        },
        {
            "caseName": "AA",
            "pairOrderData": [1, 2],
            "pairNameData": ["angle", "angle"],
        }]
    return handlePrompt(availCases, "similar")


availOptions = [
    {
        # CTPS
        "key": "Congruent",
        "other": "triangle pair snippet",
        "function": generateCTPS
    },
    {
        # STPS
        "key": "Similar",
        "other": "triangle pair snippet",
        "function": generateSTPS
    },
]


print("Welcome to {}Duc's {} generator!\n".format(
    Fore.CYAN,
    Fore.GREEN + "Geometry Snippet" + Style.RESET_ALL))


chosenIndex = 100
while chosenIndex != -1:
    # Prompt the user for input
    print("Please choose your option (-1 to exit): ")
    for index, option in enumerate(availOptions):
        print("\t{}. {} {}".format(index,
                                   Fore.CYAN + option["key"] + Style.RESET_ALL,
                                   option["other"]))
    chosenIndex = int(input("Your call: "))

    if chosenIndex == -1:
        print("Exiting, {}Bye{}!...".format(Fore.YELLOW, Style.RESET_ALL))
        break
    elif chosenIndex >= len(availOptions) or chosenIndex < 0:
        print("{}Invalid option! {}Try again...\n".format(
            Fore.RED, Style.RESET_ALL))
    else:
        # Generate snippets!
        result = availOptions[chosenIndex]["function"]()
        print("Here is the result:")
        print("{}\n".format(result))
