#!/usr/bin/env python
# coding: utf-8

# In[ ]:


title_mapping = {'Dr.': 'dr_equiv',
                 'Prof.': 'dr_equiv',
                 'Prof. Dr. Dr.': 'dr_equiv',
                 'Dipl. Ing.': 'other',
                 'Prof. Dr.': 'dr_equiv',
                 'Dr. Ing.': 'other',
                 'Dipl. Kfm.': 'other',
                 'PROF. DR': 'dr_equiv',
                 'Dr. med.': 'dr_equiv',
                 'Dr. jur.': 'dr_equiv',
                 'Dr. Rer. Nat.': 'dr_equiv',
                 'Ing.': 'other',
                 'Rechtsanwalt': 'other',
                 'Prof. Dr. Ing.': 'dr_equiv',
                 'DIPL. ING.': 'other',
                 'Dr. Phil.': 'dr_equiv',
                 'DIPL. ING': 'other',
                 'DIPL. KFM': 'other',
                 'Rechtsanwältin': 'other',
                 'Direktor': 'other',
                 'Dr. Dr.': 'dr_equiv',
                 'Mag.': 'other',
                 'Dr. Math.': 'dr_equiv',
                 'Konsul': 'other',
                 'Hofrat': 'other',
                 'DIPL. VW': 'other',
                 'DR. DR': 'dr_equiv',
                 'PROF. DR. DR': 'dr_equiv',
                 'DR. PHIL': 'dr_equiv',
                 'DR. MED': 'dr_equiv',
                 'DR. JUR': 'dr_equiv'
}

col_names = [
    'verkaufsauftrag',
     'pos_intern',
     'pos_ext',
     'oxid_id',
     'knz_urpos',
     'drerz',
     'bezper',
     'abotype',
     'erfdat',
     'liefbeginn',
     'gultig_von',
     'liefende',
     'gultig_bis',
     'erfdat_kun',
     'aart',
     'posart',
     'bezgrd',
     'preisgruppe',
     'bezgrd_lfzt',
     'bezgrd_option',
     'faktura_period',
     'werbeweg1',
     'werbeweg2',
     'werbeart', 
     'abgangs_typ',
     'lieferart',
     'zahlweg',
     'sachpramie',
     'rg',
     'we',
     'we_anrede',
     'we_titel',
     'we_ort',
     'we_land',
     'we_geburtsjahr',
     'we_optin_email',
     'we_optin_tel',
     'we_optin_brief',
     'amount'
]

channel_cat = {'Anzeigen_Eigen': 'print_display',
                'Anzeigen_Fremd': 'print_display',
                'Beilagen_Eigen': 'beilagen',
                'Beilagen_Fremd': 'beilagen',
                'CAMPAIGNING_ANZEIGEN': 'print_display',
                'CAMPAIGNING_BEILAGEN': 'beilagen',
                'CAMPAIGNING_DM': 'post',
                'CAMPAIGNING_EMAIL': 'email',
                'CAMPAIGNING_GK': 'coop',
                'CAMPAIGNING_INBOUND/DIREKT': 'inbound',
                'CAMPAIGNING_OUTBOUND': 'outbound',
                'CAMPAIGNING_OWNED DISPLAY': 'onsite',
                'CAMPAIGNING_SOCIAL (CAMP.)': 'social',
                'CAMPAIGNING_STANDWERBER': 'werber',
                'DRITTWERBER_INBOUND': 'inbound',
                'DRITTWERBER_MARKETINGPARTNER': 'coop',
                'DRITTWERBER_OUTBOUND': 'outbound',
                'DRITTWERBER_STANDWERBER': 'werber',
                'DRITTWERBER_ZWISCHENHÄNDLER': 'coop',
                'Direct Mail_Eigen': 'post',
                'Direct Mail_Fremd': 'post',
                'Direkt_na': 'inbound',
                'E-Mailing_na': 'email',
                'Firmen_na': 'coop',
                'Funk/TV_na': 'other',
                'GG_na': 'other',
                'GK_BILDUNG': 'coop',
                'GK_DIGMARKETING': 'coop',
                'GK_KAM': 'coop',
                'GK_KAM/ZWH': 'coop',
                'GK_KOOPERATIONEN': 'coop',
                'GK_KUNDENPROGRAMME': 'coop',
                'GK_NONE': 'coop',
                'GK_OUTBOUND': 'coop',
                'GK_VERANSTALTUNGEN': 'coop',
                'Gebietserw._na': 'other',
                'Inbound_na': 'inbound',
                'Internet_Aktiv': 'dig_na',
                'Internet_Passiv': 'dig_na',
                'KOOP_na': 'coop',
                'Kooperationen_Firmen': 'coop',
                'Kooperationen_Großkunden Abo': 'coop',
                'Kooperationen_Kultur': 'coop',
                'Kooperationen_Meilen': 'coop',
                'Kundenbindg._na': 'other',
                'Kündigerrück_na': 'outbound',
                'Messen_na': 'werber',
                'Nachfaßkarte_na': 'post',
                'OBJEKTM./KAM_KAM/ZWH': 'coop',
                'OBJEKTM./KAM_KUNDENPROGRAMME': 'coop',
                'OWNED_ABOSHOP': 'onsite',
                'OWNED_DISPLAY': 'onsite',
                'OWNED_EMAIL': 'email',
                'OWNED_LINKAGE': 'onsite',
                'OWNED_NONE': 'dig_na',
                'OWNED_PAYWALL': 'onsite',
                'Outbound_na': 'outbound',
                'PAID_AFFILIATE': 'affiliate',
                'PAID_DISPLAY': 'paid_display',
                'PAID_EMAIL': 'email',
                'PAID_NONE': 'dig_na',
                'PAID_OK': 'coop',
                'PAID_REM': 'dig_na',
                'PAID_SEA': 'sea',
                'PAID_SOCIALMEDIA': 'social',
                'PARTNERSHIPS_BILDUNG': 'coop',
                'PARTNERSHIPS_HOCHSCHULE': 'coop',
                'PARTNERSHIPS_KOOPERATIONEN': 'coop',
                'PAYWALL_PAYWALL': 'onsite',
                'PERFORMANCE_AFFILIATE': 'affiliate',
                'PERFORMANCE_ONSITE': 'onsite',
                'PERFORMANCE_PAID DISPLAY': 'paid_display',
                'PERFORMANCE_SEA': 'sea',
                'PERFORMANCE_SOCIAL (PERF.)': 'social',
                'PRINT_ANZEIGEN': 'print_display',
                'PRINT_BEILAGEN': 'beilagen',
                'PRINT_DIREKT': 'inbound',
                'PRINT_DM': 'post',
                'PWS_na': 'post',
                'Print_na': 'other',
                'SONSTIGE_SONDER': 'other',
                'SONSTIGE_SONSTIGE': 'other',
                'Serviceheft_na': 'other',
                'Sonder_na': 'other',
                'Sonderverkauf_na': 'other',
                'Sonstige_na': 'other',
                'Steck_na': 'post',
                'Stud_na': 'other',
                'Telefonbuch_na': 'other',
                'Telefonrechn._na': 'other',
                'Umzugsheft_na': 'other',
                'Werber_na': 'werber',
                'Wiederaufn._na': 'other',
                'Zustellerw._na': 'other',
                'na_na': 'other',
                'unbekannt_na': 'other'}

abotype_map = {'REG': 'regular',
               'REGN': 'regular',
               'STUD': 'student',
               'LWL': 'regular_friends',
               'PRN': 'free_trial',
               'PRO': 'free_trial',
               'GUA': 'gift_voucher',
               'U3NO': 'paid_trial_long',
               'U3PO': 'paid_trial_long',
               'KNO': 'paid_trial_short',
               'KPO': 'paid_trial_short',
               '3NO': 'paid_trial_short',
               '3PO': 'paid_trial_short',
               'ZWH': 'regular_coop',
               'BEF': 'paid_trial_long',
               'BUN': 'regular',
               'KOOP': 'other',
               'SOND': 'drop',
               'NONE': 'drop',
               'ZWA': 'other',
               'VERW': 'other',
               'PAT': 'other', 'KP': 'drop'}

duration_cat = {'UNBEFR': 'unlimited',
                '02-WOCH': '1month',
                '00-BEF': 'Nan',
                '04-WOCH': '1month',
                '03-WOCH': '1month',
                '13-WOCH': '3month',
                '12-WOCH': '3month',
                '08-WOCH': '2month',
                '24-TAG': '1month',
                '06-WOCH': '2month',
                'BEFR': 'Nan',
                '01-TAG': '1day',
                '30-TAG': '1month',
                '52-WOCH': 'above_3month',
                '12-MON': 'above_3month',
                '26-WOCH': 'above_3month',
                '06-MON': 'above_3month',
                '05-WOCH': '1month',
                '10-WOCH': '2month',
                '44-WOCH': 'above_3month',
                '03-MON': '3month',
                '20-WOCH': 'above_3month',
                '15-MON': 'above_3month',
                '07-MON': 'above_3month'}

delivery_cat = {'Zustellung Inl.': 'delivery_agent',
                'Keine Lieferung': 'no_delivery',
                'Post Inland': 'post',
                'Sonderzust.Inl.': 'special',
                'Großkunden': 'b2b',
                'Strb.unfrank.EU': 'foreign',
                'ZU/Ausl.': 'foreign',
                'Euro Oberfläche': 'foreign',
                'Welt Oberfläche': 'foreign',
                'Post ab Paris': 'foreign',
                'USA SEC. CLASS': 'foreign',
                'Luftpost Europa': 'foreign',
                'Madrid Abo': 'foreign',
                'Strb.unfr.WELT/': 'foreign',
                'Luftpost Welt': 'foreign'}

rebate_cat = {'35%': 'below_35pct_rebate', 
              '50%': 'above_35pct_rebate',
              'OHNE': 'na_rebate',
              '33%': 'below_35pct_rebate',
              '90%': 'above_35pct_rebate', 
              '25%': 'below_35pct_rebate',
              '20%': 'below_35pct_rebate', 
              '78%': 'above_35pct_rebate', 
              '85%': 'above_35pct_rebate', 
              '10%': 'below_35pct_rebate', 
              'UEBER 25%': 'below_35pct_rebate', 
              '75%': 'above_35pct_rebate',
              '70%': 'above_35pct_rebate',
              '33': 'below_35pct_rebate',
              '82%': 'above_35pct_rebate',
              'na': 'na_rebate'}

bezper_map = {'VA': 'weekdays_all',
              'MO-SO': 'weekday_weekend',
              'SOABO': 'sunday',
              'FRABO': 'weekday_single',
              'MO-SA': 'weekdays_all_coupon',
              '6A': 'quarterly',
              'SAABO': 'weekday_single',
              'SA-SO': 'weekend',
              'MIABO': 'weekday_single',
              'DIABO': 'weekday_single',
              'DOABO': 'weekday_single',
              'MOABO': 'weekday_single',
              'FR-SO': 'weekday_single',
              'MO-FR': 'weekday_single'}


preisgruppe_cat = {'70': 'above_35pct_rebate', 
                   '35': 'below_35pct_rebate', 
                   '32': 'below_35pct_rebate', 
                   '33': 'below_35pct_rebate', 
                   '50': 'above_35pct_rebate', 
                   '30': 'below_35pct_rebate', 
                   '37': 'above_35pct_rebate',
                   '36': 'above_35pct_rebate', 
                   '78': 'above_35pct_rebate', 
                   '65': 'above_35pct_rebate', 
                   '96': 'above_35pct_rebate', 
                   'SX': 'no_rebate', 
                   'SZ': 'above_35pct_rebate', 
                   'ST': 'no_rebate', 
                   'ZH': 'no_rebate', 
                   'Z5': 'no_rebate', 
                   'ZK': 'no_rebate', 
                   'ZJ': 'no_rebate', 
                   '99': 'no_rebate', 
                   'EB': 'above_35pct_rebate', 
                   'Z6': 'above_35pct_rebate', 
                   'SZ': 'above_35pct_rebate', 
                   'SB': 'above_35pct_rebate', 
                   'EL': 'above_35pct_rebate', 
                   'EF': 'above_35pct_rebate', 
                   'PD': 'above_35pct_rebate', 
                   '03': 'below_35pct_rebate', 
                   '02': 'below_35pct_rebate', 
                   '01': 'below_35pct_rebate', 
                   '22': 'below_35pct_rebate', 
                   '12': 'below_35pct_rebate', 
                   '06': 'below_35pct_rebate', 
                   '07': 'below_35pct_rebate', 
                   'VW': 'below_35pct_rebate', 
                   '05': 'below_35pct_rebate', 
                   'RB': 'no_rebate', 
                   'GT': 'no_rebate', 
                   'IV': 'no_rebate', 
                   'AV': 'no_rebate', 
                   'OI': 'no_rebate', 
                   '98': 'no_rebate', 
                   'SO': 'no_rebate', 
                   'ZA': 'no_rebate', 
                   'ZQ': 'no_rebate', 
                   'EH': 'no_rebate', 
                   'TS': 'no_rebate', 
                   'ZI': 'no_rebate', 
                   'BL': 'no_rebate',
                   'OR': 'no_rebate',
                   'EP': 'above_35pct_rebate',
                   'OA': 'above_35pct_rebate',
                   'SE': 'above_35pct_rebate',
                   'ES': 'above_35pct_rebate',
                   'M3': 'above_35pct_rebate',
                   'XS': 'above_35pct_rebate',
                   'ZF': 'above_35pct_rebate',
                   'SK': 'above_35pct_rebate',
                   'EN': 'above_35pct_rebate',
                   'Z8': 'above_35pct_rebate',
                   'XN': 'above_35pct_rebate',
                   'ZW': 'above_35pct_rebate',
                   '34': 'above_35pct_rebate',
                   'ZE': 'above_35pct_rebate',
                   'RV': 'above_35pct_rebate',
                   'SV': 'above_35pct_rebate',
                   'KO': 'above_35pct_rebate',
                   'GS': 'above_35pct_rebate',
                   '21': 'below_35pct_rebate',
                   'Z7': 'below_35pct_rebate',
                   '20': 'below_35pct_rebate'}

state_mapping = {'Nordrhein-Westfalen': 'nordrine_westphalia',
                'Baden-Württemberg': 'baden_wurttem',
                'Brandenburg': 'brandenburg',
                'Hessen': 'hessen',
                'Bayern': 'bavaria',
                'Niedersachsen': 'niedersachsen',
                'Rheinland-Pfalz': 'rhineland_pfalz',
                'Berlin': 'berlin',
                'Schleswig-Holstein':'schleswig_holstein',
                'Saarland': 'saarland',
                'Thüringen': 'thuringia',
                'Bremen': 'other',
                'Sachsen': 'other',
                'Schweiz': 'other',
                'Sachsen-Anhalt': 'other',
                'Norwegen': 'other',
                'Spanien': 'other',
                'Mecklenburg-Vorpommern': 'other',
                'Österreich': 'other',
                'Luxemburg': 'other',
                'Tschech. Republ': 'other',
                'Frankreich': 'other',
                ' Holstein': 'other',
                'Niederlande': 'other',
                'Italien': 'other',
                'Belgien': 'other',
                'Grossbritannien': 'other'}

