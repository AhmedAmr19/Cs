 #include <stdio.h>
 #include <ctype.h>
 #include <string.h>
 int charClass;
 char lexeme[100];
 char nextChar;
 int lexLen;
 int nextToken;
 char *input;
 int position = 0;
 void addChar();
 void getChar();
 void getNonBlank();
 int lex();
 const char* getTokenName(int token);
 #define LETTER 0
 #define DIGIT 1
 #define UNDERSCORE 2
 #define UNKNOWN 99
 #define INT_LIT 10
 #define IDENT 11
 #define ASSIGN_OP 20
 #define ADD_OP 21
 #define SUB_OP 22
 #define MULT_OP 23
 #define DIV_OP 24
 #define LEFT_PAREN 25
 #define RIGHT_PAREN 26
 int main() {
    char userInput[100];
    printf("Enter arithmetic expression (e.g., lateral_area=(volume = area * side) / 3):\n");
    fgets(userInput, sizeof(userInput), stdin);
    userInput[strcspn(userInput, "\n")] = '\0';
    input = userInput;
    getChar();
    printf("\n%-20s %-20s\n", "Lexeme", "Token");
    printf("----------------------------------------\n");
    do {
        lex();
    } while (nextToken != EOF);
    return 0;
 }
const char* getTokenName(int token) {
    switch(token) {
        case INT_LIT: return "INT_LIT";
        case IDENT: return "IDENT";
        case ASSIGN_OP: return "ASSIGN_OP";
        case ADD_OP: return "ADD_OP";
        case SUB_OP: return "SUB_OP";
        case MULT_OP: return "MULT_OP";
        case DIV_OP: return "DIV_OP";
        case LEFT_PAREN: return "LEFT_PAREN";
        case RIGHT_PAREN: return "RIGHT_PAREN";
        case EOF: return "EOF";
        default: return "UNKNOWN";
    }
 }
 int lookup(char ch) {
    switch (ch) {
        case '=':
            addChar();
            nextToken = ASSIGN_OP;
            break;
        case '(':
            addChar();
            nextToken = LEFT_PAREN;
            break;
        case ')':
            addChar();
            nextToken = RIGHT_PAREN;
            break;
        case '+':
            addChar();
            nextToken = ADD_OP;
            break;
        case '-':
            addChar();
            nextToken = SUB_OP;
            break;
        case '*':
            addChar();
            nextToken = MULT_OP;
            break;
        case '/':
            addChar();
            nextToken = DIV_OP;
            break;
        default:
            addChar();
            nextToken = EOF;
            break;
    }
    return nextToken;
 }
 void addChar() {
    if (lexLen <= 98) {
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = '\0';
}
    }
    else {
        printf("Error - lexeme is too long\n");
    }
 void getChar() {
    if (position < strlen(input)) {
        nextChar = input[position++];
        if (isalpha(nextChar)) {
            charClass = LETTER;
        }
        else if (isdigit(nextChar)) {
            charClass = DIGIT;
        }
        else if (nextChar == '_') {
            charClass = UNDERSCORE;
        }
        else {
            charClass = UNKNOWN;
        }
    }
    else {
        charClass = EOF;
    }
 }
 void getNonBlank() {
    while (isspace(nextChar)) {
        getChar();
    }
 }
 int lex() {
    lexLen = 0;
    getNonBlank();
    switch (charClass) {
        case LETTER:
        case UNDERSCORE:
            addChar();
            getChar();
            while (charClass == LETTER || charClass == DIGIT || charClass == UNDERSCORE) {
                addChar();
                getChar();
            }
            nextToken = IDENT;
            break;
        case DIGIT:
            addChar();
            getChar();
            while (charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = INT_LIT;
            break;
        case UNKNOWN:
            lookup(nextChar);
            getChar();
            break;
        case EOF:
            nextToken = EOF;
            strcpy(lexeme, "EOF");
            break;
    }
    printf("%-20s %-20s\n", lexeme, getTokenName(nextToken));
    return nextToken;
 }