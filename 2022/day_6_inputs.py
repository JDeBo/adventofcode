test_input_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_input_2 = "nppdvjthqldpwncqszvftbrmjlhg"
test_input_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
input = """
llqnqffqsqttfffbcfcbcbdcczccfssvwswrwddzlddpdhdwwlvlffjllnjjwjqwjjttwbwcwfccdmmnddgvvpwvvgsshnshsgglljfjzjpjfpfjpplddjcchdhvhlhvllvflfbllsdllgppwjjprjpjrrdwrdrggjvjppgbgttdppwhhcshsvvgpvggsllstsggdjdmjjrvjjszjsjbbsffjwjnwwzjjjvqvfftbffbpffndfdzfdfvdfdggmpmbbwgbgnnbtnnnhggdmdffrqrlrhrzzrmzzmbzzcdcwwzffsrrnfnvfnnvppwjjndjnndtdppgcppsmppljlpjjmlldlsltlglwgwcwnwvwddzrrllwjjnvjvwvppjssncnfcnfcfcczfccpjphjphjjjsgszzhthghjhrjrbrtrjrhrsrfftfzftfmmwmpmgghbggjrrsdswddtjjvnnrwrzrpzzlglwggrnrgrfftnffwwgllrqqzbqbbtltbbgdgpgphggspggplggmcmscsffzcfzzbggdrgrqgrrnlrnrbnnzsnnzcctvvnvwvnwnhhwpwtptllpflfcfttwtjjhwjhhbwhbbtppwhwvhvghvhphpwwcgwwhbbfvbffzpzlllrzlrrbnnrngrnrpnnsszbbqffpsffhfshfhzzqhhcgcgfggzmmdllthhrhnrrwggdqdsstccqllflmflfddjwjzjffvjjfgjgdgbdgdngnpgpnpffsnsjnnbbjdbjbtbmmbrrlbbqmqpqrprjjrbbvnbbzvvcwwlfwfggmhhdhsdhsdhshhqfhfrhhqlqttffpmmjzjqjggqzzdfzflfsllshhvjvfvbfvbbjljhhzrzqqszqzsqqswswbsbzszgzdgzzhjzhhvffhthvtthltthghzhvvjttczttlssvvgjjmsjstjjrfjjhbjbnjbjddqrddnbdnbnwbnbqbmqqgtgqtttcmmqbqrrgrrsrszssvpsvvjqjttjpjwwmwfwttczttgccwhcwwrzwzbwwqbqmqnmqqnfnmmmzdmzmpmssdpsslbbmgmbmlmnlldlccvzzlrzzqbqfqlflwlvlhhtrtcttgnnqhnqqtjjphjhwjhwhpwwvdvfddmndncnppcffhllfvfdfllhgslvtsqhtlfdflcjfmqbnctnfnwqrlqbzrcbvldrffcptsgslqcszqcfdvtpggvdqblwcgmdjqrpjdhtrmvrfrzznspqlfhnjsppbpjdggcwjwprpnlnntgfgmflctqphdmzfvpzzmbzmvrqdgchzmdvjdzmfsslpqvhpgznmpspjpdmlfwwjbbwqbfthghclldpmnsbcwlzswrsnfzbdzpcnrrpspdpfqhvmtfjlppqtphvzzqrwhzccnrgrtgfbfgtwvlwsmcvzmqmhsvztmmvpjzfwzgfwntbrsfthdgrcmgtdsvzcllmcshrlqldrvrnmdgbwttmhczvscrdvfgdvrhfvlghhsfbmrptbwmpnvtsrjlpjlbmmjzwwzbdtjlqqdczqgpzfjslccrcrblhplndblghchczbjjfzlsvvrqhvgdsncgpjhjlprhfhswwbmrnszqzhhlrbqpphvgtfsgmdpjwgcmqnvfdhrqmbspjpdrtdbqnbmbpgqwgmltqwrjprvsfjsmpldcqqbvmfhgzltzfvhlnfdqrphzzjrbdvnnjspvnlnnsdzvgqsqztndjpmnbqtwnpzmmfhsswwnnwwlbnpgbrhzchbnsrwwpprhntngsjzvssttqwfvjrdddtfpgtqqzcwljzmdjtgzdqjjvbqgdttdgvqvlfdsgcjhsmdmwrwdcqdflpfjbfzsvjrzrhhcnvcjblwcdvtbgfhfgcwrcjsrzcdrfwtvdqrghdtrjgdmhrfcsnwwwdpvjtpzdqfgrlmrqscjbfgdbgvflhvdjmnmslvsbcbgwplgqljmlzpgrfjwmvqfwmwrhnmdjhdwgjrngvccrbzmhcqthvvtdtmfqvfczhqbfgzgrmdtprznfzjtrcwqgztchtdmzmnwbfbnbttbvzsflcpsjshgphfdlvhdrcpsqnhjjggbnsqrfpwsdznzcwjbcswwndzbpdnfcbdrfgrmqzvtjttltbntznmqfsmqlgqvlqnrvgrnggslqhbplmgpzwlfzbvwdvrchsnhrnvgmzjdprvvspltcdzmdnlgtmrwnwpdndpdqjltcnmsggrvbprslqhfgmzqtppdpsjcmmbvfgmbpdnwdcgnssfgjhzhrjljdwhrzznscndgbscdmbbtbrnzbqzvcjgjgljbjlrrvdhjdllsnjzhwlmjslghrqplwjwssbzzpdzdfhhsqctlcddnfnnvbcwpdvzdcsgcqpctsjtdtnzpggpzsrrhfjtthqcqhtvwzltbdvdnbgwlppblwzjsqqbcpcrthhrhdnzhdnflqlvbzmcjfcrbmgdgqptfqfbmlfbblqdfmnwgvbdhmcmtmvtggqstjpwhvzjhbgpblmdrnggvrvphbglqgfcphmrgfmrwcdchtwfllqwsnbqttwdcvrwgzjfztmcffppqtmnwpgcrgwtjbdtjlmnpmvlzndljglzblwdrggqvbbfvqcbcbpqttrmqlcqnqvrfqsnlpmwlcgfwfcqpgmszfccbqtcqfwlwqrjjhrdbjqvdmfzjgncjqgqbthpgjgbfdvltbhpnbjqqwrsczrthfhmlzjjjgsjtsvgmwfsjngzfqdqzfhvwjrswvnqvsvvsjdbwlwdcsszdngmmhnnqsgvsrvpnndghrwgzztqczvhcrzdpqtrmrnfsfrlpdnbbtshfhplzqvdvzdvwhwsbpnbzlvcbgptdszjlcgfdzchjcsvhzdljvgpwstzwnssvhztcptnhslggnrschvfnmhcnjvldthtfpqzdvltfgnmtgvlrljhwqdzqfmfblstvfnpfcdsqslrqbztrbfzmsfjtjwhlzfnhrvpfqfqvtdllrvchmqphgljwcspgpwsdwqfdhsqhsflpbcbjjmjrfjrqrqfqcqzqsqcnqhfgsclfnfzblfdhphrvqdpvcqmllrcdnrlwqbrgqsbfqqllcvmglntjwcsjljgntmmldscndfdjcqpwbqpbmfjsgwfwcqbqbbhhgprlbzmvdfjcsmsqvhfhmgrhnwpslztmwbhdgrfzfcmwjswpbpzwstfbfmgwtprmptzjwtrqthrqwgslnmtlfgnvgpwvsfwthtrgwfbnnnwmdcfrpqqztplscvfnfpfwwdnfnzjccnhswwlcrrdqfhvsrnvcdrwmjswzggscplggbwgndsbntqvtrjbmbzrnbbmdjvwrmmtrmfjjhnvrcjcbqlhlthbvtjjczddblbbttmmzgdqmtdqswjdwbjhsrjbvdtqzqdbhhgbttgmgwfgfpczpqpfsddgslltwsvngwbwfbfcdzlqghwdbfzzldjpwpmpjmslwnwbrjjvwcsjgdzjwrrwnvgvrqlgjhwvrgnczspfplhfbtdpbpfqmhbvmcqdgrrjfslzgsqfpwrrrmjdtgbslddwvddrbmrdsdhhnlwsncrmnglrrpvtbrfvjbdmcpgphcdfwnfcglvmlbslttpmjnspqhnmbcqgmncfjjpdfjqhggnswbgppjhllscrvtmtmmbwbpgddtzblscntrmccdpzdnllqpvfdpfpwwvnnbjlzphvqwffwsjmbtllctrjmllwscmldcdrpfrzrqlpwbjwfgmnshzqzgdjqhcwtsqlsjffvzcpnrzmvtlzlgwvrrjtdbcnddbhjgqqzrvhplrbsrwgscjnfmhbcnpdcjqrltgdzzzzbqtsspbcdssbjrzfqdgvhmgdzsjdsqcfwbgrnhrlzgpjmhctqdccmvqzddmcptsjgtfshprqmslvtmtrprfsngrnnpnrccrvnrvcwzrbbnbghlwvcncgzglnqthchhsnzlfrcggdptvwlrbnfwgjpflgrcfzhhgffwcbhwlsdmvmsvvzvdcrlvlnstgz
"""