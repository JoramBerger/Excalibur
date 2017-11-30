from collections import OrderedDict

__all__ = ['Quantity', "QUANTITIES"]

_N_BINS_DEFAULT = "50"

DELTAR_FORMAT = "TMath::Sqrt(({a}eta-{b}eta)^2+TVector2::Phi_mpi_pi({a}phi-{b}phi)^2)"


class Quantity(object):
    def __init__(self, expression, bin_spec,
                 name=None, label=None, source_types=None, log_scale=False, channels=None):
        self.bin_spec = bin_spec
        self.label = label
        self.name = name
        self.expression = expression
        self.source_types = source_types
        self.log_scale = log_scale
        self.channels = channels

    def available_for_source_type(self, source_type):
        if self.source_types is None or source_type in self.source_types:
            return True
        return False

    def available_for_channes(self, channel):
        if self.channels is None or channel in self.channels:
            return True
        return False

    def get_bin_spec_as_string(self):
        if self.bin_spec is None:
            return None
        return ",".join(self.bin_spec)


# -- plottable quantities

QUANTITIES = dict(
    alpha=Quantity(
        name='alpha',
        expression='alpha',
        bin_spec=(_N_BINS_DEFAULT, '0', '0.5')
    ),
    e1eta=Quantity(
        name='e1eta',
        expression='e1eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        channels=['Zee']
    ),
    e1iso=Quantity(
        name='e1iso',
        expression='e1iso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zee']
    ),
    e1pt=Quantity(
        name='e1pt',
        expression='e1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        channels=['Zee']
    ),
    e2pt=Quantity(
        name='e2pt',
        expression='e2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        channels=['Zee']
    ),
    eminusiso=Quantity(
        name='eminusiso',
        expression='eminusiso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zee']
    ),
    eplusiso=Quantity(
        name='eplusiso',
        expression='eplusiso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zee']
    ),
    genjet1eta=Quantity(
        name='genjet1eta',
        expression='genjet1eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{GenJet1}$',
        source_types=['MC']
    ),
    genjet1pt=Quantity(
        name='genjet1pt',
        expression='genjet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '250'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{GenJet1}~/~GeV$',
        source_types=['MC']
    ),
    genjet2eta=Quantity(
        name='genjet2eta',
        expression='genjet2eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{GenJet2}$',
        source_types=['MC']
    ),
    genjet2pt=Quantity(
        name='genjet2pt',
        expression='genjet2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '50'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{GenJet2}~/~GeV$',
        source_types=['MC']
    ),
    jet1area=Quantity(
        name='jet1area',
        expression='jet1area',
        bin_spec=(_N_BINS_DEFAULT, '0.3', '0.7')
    ),
    jet1chf=Quantity(
        name='jet1chf',
        expression='jet1chf',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF charged hadron fraction (Jet 1)',
        log_scale=True
    ),
    jet1ef=Quantity(
        name='jet1ef',
        expression='jet1ef',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF electron fraction (Jet 1)',
        log_scale=True
    ),
    jet1eta=Quantity(
        name='jet1eta',
        expression='jet1eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{Jet1}$'
    ),
    jet1eta_extended=Quantity(
        name='jet1eta_extended',
        expression='jet1eta',
        bin_spec=(_N_BINS_DEFAULT, '-9', '9'),
        label='$\\\\eta^\\\\mathrm{Jet1}$'
    ),
    jet1hfem=Quantity(
        name='jet1hfem',
        expression='jet1hfem',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF HF em fraction (Jet 1)',
        log_scale=True
    ),
    jet1hfhf=Quantity(
        name='jet1hfhf',
        expression='jet1hfhf',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF HF hadronic fraction (Jet 1)',
        log_scale=True
    ),
    jet1mf=Quantity(
        name='jet1mf',
        expression='jet1mf',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF muon fraction (Jet 1)',
        log_scale=True
    ),
    jet1nhf=Quantity(
        name='jet1nhf',
        expression='jet1nhf',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF neutral hadron fraction (Jet 1)',
        log_scale=True
    ),
    jet1pf=Quantity(
        name='jet1pf',
        expression='jet1pf',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='PF photon fraction (Jet 1)',
        log_scale=True
    ),
    jet1phi=Quantity(
        name='jet1phi',
        expression='jet1phi',
        bin_spec=(_N_BINS_DEFAULT, '-4', '4')
    ),
    jet1pt=Quantity(
        name='jet1pt',
        expression='jet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '250'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet1}~/~GeV$'
    ),
    jet1pt_extended=Quantity(
        name='jet1pt_extended',
        expression='jet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '700'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet1}~/~GeV$'
    ),
    jet1pt_extended_log=Quantity(
        name='jet1pt_extended_log',
        expression='jet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '700'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet1}~/~GeV$',
        log_scale=True
    ),
    jet1ptl1=Quantity(
        name='jet1ptl1',
        expression='jet1ptl1',
        bin_spec=(_N_BINS_DEFAULT, '0', '250')
    ),
    jet1pt_over_jet1ptraw=Quantity(
        name='jet1pt_over_jet1ptraw',
        expression='jet1pt/jet1ptraw',
        label=r"$p_\\mathrm{T}^\\mathrm{Jet1, corr}/p_\\mathrm{T}^\\mathrm{Jet1, raw}$",
        bin_spec=(_N_BINS_DEFAULT, '0.95', '1.25')
    ),
    jet1res=Quantity(
        name='jet1res',
        expression='jet1res',
        bin_spec=(_N_BINS_DEFAULT, '0.', '2.')
    ),
    jet2eta=Quantity(
        name='jet2eta',
        expression='jet2eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{Jet2}$'
    ),
    jet2eta_extended=Quantity(
        name='jet2eta_extended',
        expression='jet2eta',
        bin_spec=(_N_BINS_DEFAULT, '-9', '9'),
        label='$\\\\eta^\\\\mathrm{Jet2}$'
    ),
    jet2phi=Quantity(
        name='jet2phi',
        expression='jet2phi',
        bin_spec=(_N_BINS_DEFAULT, '-4', '4')
    ),
    jet2pt=Quantity(
        name='jet2pt',
        expression='jet2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '50'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet2}~/~GeV$'
    ),
    jet2pt_extended=Quantity(
        name='jet2pt_extended',
        expression='jet2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '150'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet2}~/~GeV$'
    ),
    jet2pt_extended_log=Quantity(
        name='jet2pt_extended_log',
        expression='jet2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '150'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet2}~/~GeV$',
        log_scale=True
    ),
    jet2pt_over_jet1pt=Quantity(
        name='jet2pt_over_jet1pt',
        expression='jet2pt/jet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '1'),
        label='jet1pt/jet2pt'
    ),
    jet3eta=Quantity(
        name='jet3eta',
        expression='jet3eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{Jet3}$'
    ),
    jet3eta_extended=Quantity(
        name='jet3eta_extended',
        expression='jet3eta',
        bin_spec=(_N_BINS_DEFAULT, '-9', '9'),
        label='$\\\\eta^\\\\mathrm{Jet3}$'
    ),
    jet3phi=Quantity(
        name='jet3phi',
        expression='jet3phi',
        bin_spec=(_N_BINS_DEFAULT, '-4', '4'),
        label='$\\\\phi^\\\\mathrm{Jet3}$'
    ),
    jet3pt=Quantity(
        name='jet3pt',
        expression='jet3pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '50'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet3}~/~GeV$'
    ),
    jet3pt_extended=Quantity(
        name='jet3pt_extended',
        expression='jet3pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet3}~/~GeV$'
    ),
    jet3pt_extended_log=Quantity(
        name='jet3pt_extended_log',
        expression='jet3pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{Jet3}~/~GeV$',
        log_scale=True
    ),
    jetHT=Quantity(
        name='jetHT',
        expression='jetHT',
        bin_spec=(_N_BINS_DEFAULT, '0', '0.5')
    ),
    matchedgenjet1eta=Quantity(
        name='matchedgenjet1eta',
        expression='matchedgenjet1eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{MatchedGenJet1}$',
        source_types=['MC']
    ),
    matchedgenjet1pt=Quantity(
        name='matchedgenjet1pt',
        expression='matchedgenjet1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '250'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{MatchedGenJet1}~/~GeV$',
        source_types=['MC']
    ),
    matchedgenjet2eta=Quantity(
        name='matchedgenjet2eta',
        expression='matchedgenjet2eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{MatchedGenJet2}$',
        source_types=['MC']
    ),
    matchedgenjet2pt=Quantity(
        name='matchedgenjet2pt',
        expression='matchedgenjet2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '50'),
        label='$p_\\\\mathrm{T}^\\\\mathrm{MatchedGenJet2}~/~GeV$',
        source_types=['MC']
    ),
    met=Quantity(
        name='met',
        expression='met',
        bin_spec=(_N_BINS_DEFAULT, '0', '100')
    ),
    metphi=Quantity(
        name='metphi',
        expression='metphi',
        bin_spec=(_N_BINS_DEFAULT, '-4', '4')
    ),
    mpf=Quantity(
        name='mpf',
        expression='mpf',
        bin_spec=(_N_BINS_DEFAULT, '0', '2')
    ),
    mu1eta=Quantity(
        name='mu1eta',
        expression='mu1eta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        channels=['Zmm']
    ),
    mu1iso=Quantity(
        name='mu1iso',
        expression='mu1iso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zmm']
    ),
    mu1pt=Quantity(
        name='mu1pt',
        expression='mu1pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        channels=['Zmm']
    ),
    mu2pt=Quantity(
        name='mu2pt',
        expression='mu2pt',
        bin_spec=(_N_BINS_DEFAULT, '0', '100'),
        channels=['Zmm']
    ),
    muminusiso=Quantity(
        name='muminusiso',
        expression='muminusiso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zmm']
    ),
    muplusiso=Quantity(
        name='muplusiso',
        expression='muplusiso',
        bin_spec=(_N_BINS_DEFAULT, '0', '2'),
        channels=['Zmm']
    ),
    njets=Quantity(
        name='njets',
        expression='njets',
        bin_spec=('161', '-0.5', '160.5'),
        label='# of jets'
    ),
    njets10=Quantity(
        name='njets10',
        expression='njets10',
        bin_spec=('31', '-0.5', '30.5'),
        label='# of jets with $p_T>10$ GeV'
    ),
    njets10_log=Quantity(
        name='njets10_log',
        expression='njets10',
        bin_spec=('31', '-0.5', '30.5'),
        label='# of jets with $p_T>10$ GeV',
        log_scale=True
    ),
    njets30=Quantity(
        name='njets30',
        expression='njets30',
        bin_spec=('6', '-0.5', '5.5'),
        label='# of jets with $p_T>30$ GeV'
    ),
    njets30_log=Quantity(
        name='njets30_log',
        expression='njets30',
        bin_spec=('6', '-0.5', '5.5'),
        label='# of jets with $p_T>30$ GeV',
        log_scale=True
    ),
    njets_log=Quantity(
        name='njets_log',
        expression='njets',
        bin_spec=('161', '-0.5', '160.5'),
        label='# of jets'
    ),
    npu=Quantity(
        name='npu',
        expression='npu',
        bin_spec=('61', '-0.5', '60.5'),
        source_types=['MC']
    ),
    npu_log=Quantity(
        name='npu_log',
        expression='npu',
        bin_spec=('61', '-0.5', '60.5'),
        source_types=['MC'],
        log_scale=True
    ),
    npumean=Quantity(
        name='npumean',
        expression='npumean',
        bin_spec=(_N_BINS_DEFAULT, '0', '60'),
        source_types=['MC']
    ),
    npumean_log=Quantity(
        name='npumean_log',
        expression='npumean',
        bin_spec=(_N_BINS_DEFAULT, '0', '60'),
        source_types=['MC'],
        log_scale=True
    ),
    npv=Quantity(
        name='npv',
        expression='npv',
        bin_spec=('61', '-0.5', '60.5')
    ),
    npv_log=Quantity(
        name='npv_log',
        expression='npv',
        bin_spec=('61', '-0.5', '60.5'),
        log_scale=True
    ),
    ptbalance=Quantity(
        name='ptbalance',
        expression='ptbalance',
        bin_spec=(_N_BINS_DEFAULT, '0', '2')
    ),
    run=Quantity(
        name='run',
        expression='run',
        bin_spec=('120', '272007', '284044')
    ),
    runBCD=Quantity(
        name='runBCD',
        expression='run',
        bin_spec=('48', '272007', '276811')
    ),
    zeta=Quantity(
        name='zeta',
        expression='zeta',
        bin_spec=(_N_BINS_DEFAULT, '-5', '5'),
        label='$\\\\eta^\\\\mathrm{Z}$'
    ),
    zphi=Quantity(
        name='zphi',
        expression='zphi',
        bin_spec=(_N_BINS_DEFAULT, '-4', '4')
    ),
    zmass=Quantity(
        name='zmass',
        expression='zmass',
        bin_spec=(_N_BINS_DEFAULT, '70', '110')
    ),
    zpt=Quantity(
        name='zpt',
        expression='zpt',
        bin_spec=(_N_BINS_DEFAULT, '1', '150')
    ),
    zpt_low=Quantity(
        name='zpt_low',
        expression='zpt',
        bin_spec=(_N_BINS_DEFAULT, '15', '80')
    ),
)

# --------------------------------------------------------------

_obj_dicts = OrderedDict(
    jet1={
        "label": "Jet1",
    },
    jet2={
        "label": "Jet2",
    },
    jet3={
        "label": "Jet3",
    },
    z={
        "label": "Z",
    },
    mu1={
        "label": r"\\mu_1",
        "channels": ["Zmm"]
    },
    mu2={
        "label": "\\mu_2",
        "channels": ["Zmm"]
    },
    e1={
        "label": "e_1",
        "channels": ["Zee"]
    },
    e2={
        "label": "e_2",
        "channels": ["Zee"]
    },

    #
    genjet1={
        "label": "GenJet1",
        "source_types": ["MC"]
    },
    genjet2={
        "label": "GenJet2",
        "source_types": ["MC"]
    },
    matchedgenjet1={
        "label": "MatchedGenJet1",
        "source_types": ["MC"]
    },
    matchedgenjet2={
        "label": "MatchedGenJet2",
        "source_types": ["MC"]
    },
)


# --

_delta_expr_dicts = {
    "deltaPhi" : {
        "label": r"\\Delta \\phi",
        "expr_lambda": lambda a, b: "TVector2::Phi_mpi_pi({a}phi-{b}phi)".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "-3.14159", "3.14159")
    },
    "absDeltaPhi" : {
        "label": r"|\\Delta \\phi|",
        "expr_lambda": lambda a, b: "abs(TVector2::Phi_mpi_pi({a}phi-{b}phi))".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "3.14159")
    },
    "absDeltaPhi_aroundPi" : {
        "label": r"|\\Delta \\phi|",
        "expr_lambda": lambda a, b: "abs(TVector2::Phi_mpi_pi({a}phi-{b}phi))".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "2.74159", "3.14159")
    },
    "absDeltaPhi_fine" : {  # fine binning
        "label": r"|\\Delta \\phi|",
        "expr_lambda": lambda a, b: "abs(TVector2::Phi_mpi_pi({a}phi-{b}phi))".format(a=a, b=b),
        "bins": ("250", "0", "3.14159")
    },
    "absDeltaPhi_aroundPi_fine" : {  # fine binning
        "label": r"|\\Delta \\phi|",
        "expr_lambda": lambda a, b: "abs(TVector2::Phi_mpi_pi({a}phi-{b}phi))".format(a=a, b=b),
        "bins": ("250", "2.74159", "3.14159")
    },
    "deltaEta" : {
        "label": r"\\Delta \\eta",
        "expr_lambda": lambda a, b: "{a}eta-{b}eta".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "-10", "10")
    },
    "absDeltaEta" : {
        "label": r"|\\Delta \\eta|",
        "expr_lambda": lambda a, b: "abs({a}eta-{b}eta)".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "10")
    },
    "deltaR" : {
        "label": r"\\Delta R",
        "expr_lambda": lambda a, b: DELTAR_FORMAT.format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "10")
    },
    "deltaR_aroundZero" : {
        "label": r"\\Delta R",
        "expr_lambda": lambda a, b: DELTAR_FORMAT.format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "0.1")
    },
    "deltaR_upToOne" : {
        "label": r"\\Delta R",
        "expr_lambda": lambda a, b: DELTAR_FORMAT.format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "1.0")
    },
    "deltaPtRel" : {
        "label": r"\\Delta p_{\\mathrm{T}}/p_{\\mathrm{T}}",
        "expr_lambda": lambda a, b: "({a}pt-{b}pt)/{a}pt".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "1")
    },
    "pTAsymmetry" : {
        "label": r"A_{p,\\mathrm{T}}",
        "expr_lambda": lambda a, b: "({a}pt-{b}pt)/({a}pt+{b}pt)".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "1")
    },
    "pTRatio" : {
        "label": r"Ratio_{p,\\mathrm{T}}",
        "expr_lambda": lambda a, b: "{a}pt/{b}pt".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "10")
    },
    "pTRatio_aroundOne" : {
        "label": r"Ratio_{p,\\mathrm{T}}",
        "expr_lambda": lambda a, b: "{a}pt/{b}pt".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0.5", "3")
    },
    "sumEta" : {
        "label": r"\\Sigma \\eta",
        "expr_lambda": lambda a, b: "{a}eta+{b}eta".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "-10", "10")
    },
    "absSumEta" : {
        "label": r"|\\Sigma \\eta|",
        "expr_lambda": lambda a, b: "abs({a}eta+{b}eta)".format(a=a, b=b),
        "bins": (_N_BINS_DEFAULT, "0", "10")
    },
}

for _obj1, _obj1_dict in _obj_dicts.iteritems():
    for _obj2, _obj2_dict in _obj_dicts.iteritems():
        if _obj1 == _obj2:
            continue

        _channels_1 = _obj1_dict.get("channels", None)
        _channels_2 = _obj2_dict.get("channels", None)

        if _channels_1 is None and _channels_2 is None:
            _channels = None
        elif _channels_1 is None and _channels_2 is not None:
            _channels =  set(_channels_2)
        elif _channels_1 is not None and _channels_2 is None:
            _channels =  set(_channels_1)
        else:
            _channels =  set(_channels_1).intersection(set(_channels_2))

        _source_types_1 = _obj1_dict.get("source_types", None)
        _source_types_2 = _obj2_dict.get("source_types", None)

        if _source_types_1 is None and _source_types_2 is None:
            _source_types = None
        elif _source_types_1 is None and _source_types_2 is not None:
            _source_types =  set(_source_types_2)
        elif _source_types_1 is not None and _source_types_2 is None:
            _source_types =  set(_source_types_1)
        else:
            _source_types =  set(_source_types_1).intersection(set(_source_types_2))

        for _delta_expr, _delta_expr_dict in _delta_expr_dicts.iteritems():
            _key = r"{}_{}_{}".format(_delta_expr, _obj1, _obj2)
            _label = r"${}({},{})$".format(_delta_expr_dict['label'], _obj1_dict['label'], _obj2_dict['label'])
            _kwargs = {}
            if _channels:
                _kwargs['channels'] = list(_channels)
            if _source_types:
                _kwargs['source_types'] = list(_source_types)
            QUANTITIES[_key] = Quantity(
                expression=_delta_expr_dict['expr_lambda'](_obj1, _obj2),
                label=_label,
                bin_spec=_delta_expr_dict['bins'],
                **_kwargs
            )


# manual tweaks
QUANTITIES['deltaEta_matchedgenjet1_jet1'].bin_spec = (_N_BINS_DEFAULT, "-1", "1")
QUANTITIES['deltaEta_matchedgenjet2_jet2'].bin_spec = (_N_BINS_DEFAULT, "-1", "1")