from pbs_decode import dekodovat_pbs



def test_pbs_decoding():
    """
        Tests PAY by Square decoding
    """

    # Example decoded QR code from https://bsqr.co/generator-test/
    example_string = "0004S00064DPF23L21L6HK0S4QSL8KDATUPGVMT2K2AQ705BFAT6UFLILGRR8UGR97P2UPCR7III88BU3400"
    decoded = dekodovat_pbs(example_string)
    print(decoded)



if __name__ == "__main__":
    test_pbs_decoding()
