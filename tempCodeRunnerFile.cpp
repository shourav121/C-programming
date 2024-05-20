

    cout << endl;
    account.withdraw(200.0);
    account.display();

    cout << endl;
    account.withdraw(2000.0); // Attempting to withdraw more than balance
    account.display();

    cout << endl;
    // Using the inline function to check if the account is in overdraft
    if (account.isOverdraft()) {
        cout << "Account is in overdraft!" << endl;
    } else {
        cout << "Account is not in overdraft." << endl;
    }

    return 0;
}
