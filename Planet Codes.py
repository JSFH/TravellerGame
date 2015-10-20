'''
Jamie Farhi-Humphrey
Program to produce pertinent information regard Traveller planets/systems from
the planetary codes. Reference guide utilized;
http://www.mediafire.com/view/ge55ff7u0hhq77m/UWP_guide_(how_to_read_planetary_stats).pdf
Intent was using Mongoose Traveller (what I understand to be called 4e)
I'm not as familiar with Traveller as I would like.'''

'''Starport table. Gives starship accommodations available on the given planet.
First and most important assuming you're considering visiting with your ship.
Input is characters a-e, or x.'''
def starport(strprt):
    print '#'*23+'STARPORT QUALITY'+'#'*23
    if strprt.upper() == 'A':
        print strprt.upper()
        print 'Excellent Quality. Refined Fuel available. Annual maintenance'
        print 'overhaul available. Shipyard capable of constructing starships'
        print 'and non-starships present. Naval Base and/or Scout Base may be'
        print 'present. TAS present.'

    elif strprt.upper() == 'B':
        print strprt.upper()
        print 'Good Quality. Refined fuel available. Annual maintenance'
        print 'overhaul available. Shipyard capable of constructing non-'
        print 'starships present. Naval base and/or scout base may be'
        print 'present. Traveller\'s Aid Society present.'

    elif strprt.upper() == 'C':
        print strprt.upper()
        print 'Routine Quality. Only unrefined fuel available. Reasonable '
        print 'repair facilities present. Scout base may be present.'

    elif strprt.upper() == 'D':
        print strprt.upper()
        print 'Poor Quality. Only unrefined fuel available. No repair'
        print 'facilities present. Scout base may be present.'

    elif strprt.upper() == 'E':
        print strprt.upper()
        print 'Frontier Installation. Essentially a marked spot of bedrock'
        print 'with no fuel, facilities, or bases present.'

    elif strprt.upper() == 'X':
        print strprt.upper()
        print 'No Starport. No provision is made for any ship landings.'
        

    else:
        print 'Improper starport code value; check code composition'

'''Dimensions table. Copied verbatim from the Traveller reference table.
Painstakingly formatted to be mildly parseable. Digits or character a. '''
def size(szky):
    print '#########################MEASUREMENTS#########################'
    print '##Size###Diam.(km)####Mass####Area####Gravity###Escape Velo.##'
    if szky=='1':
        print '#  '+szky+'   #  1,600    # 0.0019 # 0.015 #  0.122  #  1.35 (km/s) #'
    elif szky=='2':
        print '#  '+szky+'   #  3,200    # 0.015  # 0.063 #  0.240  #  2.69 (km/s) #'
    elif szky=='3':
        print '#  '+szky+'   #  4,800    # 0.053  # 0.141 #  0.377  #  4.13 (km/s) #'
    elif szky=='4':
        print '#  '+szky+'   #  6,400    # 0.125  # 0.250 #  0.500  #  5.49 (km/s) #'
    elif szky=='5':
        print '#  '+szky+'   #  8,000    # 0.244  # 0.391 #  0.625  #  6.87 (km/s) #'
    elif szky=='6':
        print '#  '+szky+'   #  9,600    # 0.422  # 0.563 #  0.840  #  8.72 (km/s) #'
    elif szky=='7':
        print '#  '+szky+'   # 11,200    # 0.670  # 0.766 #  0.875  #  9.62 (km/s) #'
    elif szky=='8':
        print '#  '+szky+'   # 12,800    # 1.000  # 1.000 #  1.000  # 11.00 (km/s) #'
    elif szky=='9':
        print '#  '+szky+'   # 14,400    # 1.424  # 1.266 #  1.120  # 12.35 (km/s) #'
    elif szky.upper() == 'A':
        print '#  '+szky.upper()+'  # 16,000    # 1.953  # 1.563 #  1.250  # 13.73 (km/s) #'
    else:
        print 'Not registered; check input'

'''Atmospherics. Forgot to do this, it seems. input is 0-f'''
def Atmo(sph):
    print '#'*25 + 'ATMOSPHERICS' + '#'*25
    if sph == '0':
        print 'No atmosphere.Requires vacc suit.'
    elif sph == '1':
        print 'Trace. Requires vacc suit.'
    elif sph == '2':
        print 'Very thin. Tainted. Requires combination respirator/filter.'
    elif sph == '3':
        print 'Very thin. Requires respirator.'
    elif sph == '4':
        print 'Thin. Tainted. Requires filter mask.'
    elif sph == '5':
        print 'Thin. Breathable.'
    elif sph == '6':
        print 'Standard. Breathable.'
    elif sph == '7':
        print 'Standard. Tainted. Requires filter mask.'
    elif sph == '8':
        print 'Dense. Breathable.'
    elif sph == '9':
        print 'Dense. Tainted. Requires filter mask.'
    elif sph.upper() == 'A':
        print 'Exotic. Requires special protective equipment.'
    elif sph.upper() == 'B':
        print 'Corrosive. Requires protective suit.'
    elif sph.upper() == 'C':
        print 'Insidious. Requires protective suit.'
    elif sph.upper() == 'D':
        print 'Dense, high. Breathable above a minimum altitude.'
    elif sph.upper() == 'E':
        print 'Ellipsoid. Breathable at certain altitudes.'
    elif sph.upper() == 'F':
        print 'Thin, low. Breathable below certain altitudes.'
    else:
        print 'Atmospherics Key not parseable. check input.'
    

'''Very simple hydrographics table. Commentary only in two cases.
Variable+string concatenation in most cases. Accepts single digits or character a'''
def Hydro(wtr):
    print '#'*25+'HYDROGRAPHICS'+'#'*24
    if (wtr=='0') or wtr=='1' or wtr=='2' or wtr=='3'or wtr=='4'or wtr=='5'or wtr=='6' or wtr=='8' or wtr=='9':
        print wtr+'0% water.'
    elif wtr=='7':
        print wtr+'0% water. Equivalent to Terra or Vland.'
    elif wtr.upper() == 'A':
        print '100% water. Water world.'
    else:
        print 'Invalid Hydrographics key, check input code.'

'''How many blokes live there. Digit is the population exponent; alternate reading
population == x * 10^[pop exponent]. 3 can therefore be 100 inhabitants, 549, or 999.
0-9 and A accepted'''
def popu (pexp):
    print '#'*26 +'POPULATION'+'#'*26
    if pexp=='0':
        print 'Few or no inhabitants.                                     0'
    elif pexp=='1':
        print 'Tens of inhabitants.                                      10'
    elif pexp=='2':
        print 'Hundreds of inhabitants.                                 100'
    elif pexp=='3':
        print 'Thousnds of inhabitants.                               1,000'
    elif pexp=='4':
        print 'Tens of thousands of inhabitants.                     10,000'
    elif pexp=='5':
        print 'Hundreds of thousands of inhabitants.                100,000'
    elif pexp=='6':
        print 'Millions of inhabitants.                           1,000,000'
    elif pexp=='7':
        print 'Tens of millions of inhabitants                   10,000,000'
    elif pexp=='8':
        print 'Hundreds of millions of inhabitants.             100,000,000'
    elif pexp=='9':
        print 'Billions of inhabitants.                       1,000,000,000'
    elif pexp.upper() == 'A':
        print 'Tens of billions of inhabitants               10,000,000,000'
    else:
        print 'Population key wrong. Check code input.'

'''Boy howdy. Planetary governments. Awful lot of them. Single digit or character,
though not all characters have entries. Open to expansion. Probably draws on a lot of
sourcebooks. 0-9, a-h, j-n, p-u, w, x have entries.'''
def Government(gtype):
    print 'DESCRIPTION'+'#'*41+'ALLEGIANCE'
    if gtype=='0':
        print 'No Government Structure'
    elif gtype=='1':
        print 'Company/Corporation'
    elif gtype=='2':
        print 'Participating Democracy'
    elif gtype=='3':
        print 'Self-Perpetuating Oligarchy'
    elif gtype=='4':
        print 'Representative Democracy'
    elif gtype=='5':
        print 'Feudal Technocracy'
    elif gtype=='6':
        print 'Captive Government / Colony'
    elif gtype=='7':
        print 'Balkanization'
    elif gtype=='8':
        print 'Civil Service Bureacracy'
    elif gtype=='9':
        print 'Impersonal Bureacracy'
    elif gtype.upper() == 'A':
        print 'Charismatic Dictator'
    elif gtype.upper() == 'B':
        print 'Non-Charismatic Dictator'
    elif gytpe.upper() == 'C':
        print 'Charismatic Oligarchy'
    elif gtype.upper() == 'D':
        print 'Religious Dictatorship'
    elif gtype.upper() == 'E':
        print 'Religious Autocracy'
    elif gtype.upper() == 'F':
        print 'Totalitarian Oligarchy'
    elif gtype.upper() == 'G':
        print 'Small Station or Facility'+' '*34 +'Aslan'
    elif gtype.upper() == 'H':
        print 'Split Clan Control'+ ' '*46 +'Aslan'
    elif gtype.upper() == 'J':
        print 'Single On-world Clan Control'+' '*31+'Aslan'
    elif gtype.upper() == 'K':
        print 'Single Multi-world Clan Control'+' '*28+'Aslan'
    elif gtype.upper() == 'L':
        print 'Major Clan Control'+' '*46+'Aslan'
    elif gtype.upper() == 'M':
        print 'Vassal Clan Control'+' '*40+'Aslan'
    elif gtype.upper() == 'N':
        print 'Major Vassal Clan Control'+' '*30+'Aslan'
    elif gtype.upper() == 'P':
        print 'Small Station or Facility'+' '*33+'K\'kree'
    elif gtype.upper() == 'Q':
        print 'Split Clan Control'+' '*40+'K\'kree'
    elif gtype.upper() == 'R':
        print 'Steppelord On-world Rule'+' '*34+'K\'kree'
    elif gtype.upper() == 'S':
        print 'Sept'+' '*55+'Hiver'
    elif gtype.upper() == 'T':
        print 'Unsupervised Anarchy'+' '*39 +'Hiver'
    elif gtype.upper() == 'U':
        print 'Supervised Anarchy'+' '*41+'Hiver'
    elif gtype.upper() == 'W':
        print 'Committee'+' '*50+'Hiver'
    elif gtype.upper() == 'X':
        print 'Droyne Hierarchy'+' '*42+'Droyne'
    else:
        print 'Error: Unlisted. Check sourcebooks or planetary code input.'


'''Law Level; Not totally sure how to parse the results, but copied from book table
anyway. Accepts 0-9, a-h, j-l, and s for special.'''
def LawL(lev):
    print '#'*27+'Law Level'+'#'*26
    if lev == '0':
        print 'No Prohibitions'
    elif lev == '1':
        print 'Body pistols, explosives, and poison gas prohibited.'
    elif lev == '2':
        print 'Portable energy weapons prohibited.'
    elif lev == '3':
        print 'Machine guns, automatic rifles prohibited.'
    elif lev == '4':
        print 'Light assault weapons prohibited.'
    elif lev == '5':
        print 'Personal concealable weapons prohibited.'
    elif lev == '6':
        print 'All firearms except shotguns prohibited.'
    elif lev == '7':
        print 'Shotguns Prohibited.'
    elif lev == '8':
        print 'Long bladed weapons controlled; open possession prohibited.'
    elif lev == '9':
        print 'Possession of weapons outside the home prohibited.'
    elif lev.upper() == 'A':
        print 'Weapon posession prohibited.'
    elif lev.upper() == 'B':
        print 'Rigid control of civilian movement.'
    elif lev.upper() == 'C':
        print 'Unrestricted invasion of privacy.'
    elif lev.upper() == 'D':
        print 'Paramilitary law enforcement.'
    elif lev.upper() == 'E':
        print 'Full-fledged police state.'
    elif lev.upper() == 'F':
        print 'All facets of daily life regularly legislated and controlled.'
    elif lev.upper() == 'G':
        print 'Severe punishment for petty infractions.'
    elif lev.upper() == 'H':
        print 'Legalized oppressive practices.'
    elif lev.upper() == 'J':
        print 'Routinely oppressive and restrictive.'
    elif lev.upper() == 'K':
        print 'Excessively oppressive and restrictive.'
    elif lev.upper() == 'L':
        print 'Totally oppressive and restrictive.'
    elif lev.upper() == 'S':
        print 'Special/Variable situation.'
    else:
        print 'Key not recognized, check sourcebooks and input.'


'''Tech Level. 0-9, a-f. Kinda weird delineations, but interseting too. I'm assuming
'present day' doesn't refer to 1970 when Traveller was first published.'''

def TechLev(tek):
    print '#'*22+'TECHNOLOGICAL LEVEL'+'#'*21
    if tek == '0':
        print 'Stone Age. Primitive.'
    elif tek == '1':
        print 'Bronze, Iron. Bronze Age to middle Ages.'
    elif tek == '2':
        print 'Printing Press.'
    elif tek == '3':
        print 'Basic Science.'
    elif tek == '4':
        print 'Internal Combustion.'
    elif tek == '5':
        print 'Mass Production.'
    elif tek == '6':
        print 'Nuclear Power.'
    elif tek == '7':
        print 'Miniaturized Electronics.'
    elif tek == '8':
        print 'Quality Computers. Present Day.'
    elif tek == '9':
        print 'Anti-Gravity. Near Future.'
    elif tek.upper() == 'A':
        print 'Interstellar community.'
    elif tek.upper() == 'B':
        print 'Lower Average Imperial.'
    elif tek.upper() == 'C':
        print 'Average Imperial.'
    elif tek.upper() == 'D':
        print 'Above Average Imperial.'
    elif tek.upper() == 'E':
        print 'Extra-Above Average Imperial.'
    elif tek.upper() == 'F':
        print 'Technical Imperial Maximum.'
    else:
        print 'Not Found, check sourcebooks or input.'

'''int main(){
Gets a code; does not test for length or proper content. Starts shunting pieces off
to the various subfunctions in order. Will continue even if a function is fed wrong.
Crude attempt to accommodate for the A788899-C and A788899C formats. Yay, python!'''
planetcode=raw_input('Enter Code: ')
starport(planetcode[0])
size(planetcode[1])
Atmo(planetcode[2])
Hydro(planetcode[3])
popu(planetcode[4])
Government(planetcode[5])
LawL(planetcode[6])
if planetcode[7] == '-':
    TechLev(planetcode[8])
else:
    TechLev(planetcode[7])
#Time to do Trade Codes!
#could do as a function, but would have to feed whole code to it, so why bother?
print '#'*64
if (planetcode[2].upper()=='A' or planetcode[2].upper()=='B' or planetcode[2].upper()=='C' or planetcode[2].upper()=='D' or planetcode[2].upper()=='E' or planetcode[2].upper()=='F' or planetcode[5].upper()=='0' or planetcode[5].upper()=='7' or planetcode[5].upper()=='A' or planetcode[6].upper()=='0' or planetcode[6].upper()=='9' or planetcode[6].upper()=='A' or planetcode[6].upper()=='B' or planetcode[6].upper()=='C' or planetcode[6].upper()=='D' or planetcode[6].upper()=='E' or planetcode[6].upper()=='F' or planetcode[6].upper()=='G' or planetcode[6].upper()=='H' or planetcode[6].upper()=='J' or planetcode[6].upper()=='K' or planetcode[6].upper()=='L' or planetcode[6].upper()=='S'):
    print "CONSIDER AMBER TRAVEL CODE"
print '#'*27+'TRADE CODE'+'#'*27
if (52<=planetcode[2]<=57):
    print "got here"
    if(52<=planetcode[3]<=56):
        if (53<=planetcode[4]<=55):
            print 'Agricultural - Ag - Agricultural worlds are dedicated to'
            print 'farming and food production. Often, they are divided into vast'
            print 'semi-fuedal estates.'
        if (planetcode[1]>=5):
            print 'Garden - Ga -Garden worlds are Earthlike.'
if (planetcode[1]==48 and planetcode[2]==48 and planetcode[3]==48):
    print 'Asteroid - As - Asteroids are usually mining colonies, but can'
    print 'also be orbital factories or colonies.'

    

