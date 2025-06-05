import { useState, useEffect } from 'react';
import {
  Box,
  VStack,
  HStack,
  Heading,
  Text,
  Button,
  Alert,
  AlertIcon,
  Grid,
  GridItem,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  Badge,
  Stat,
  StatLabel,
  StatNumber,
  StatHelpText,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Card,
  CardHeader,
  CardBody,
  Select,
  Skeleton,
  SkeletonText,
  useToast,
  Tooltip,
  SimpleGrid,
  Divider
} from '@chakra-ui/react';
import { InfoIcon, WarningIcon, ChevronDownIcon, ChevronUpIcon } from '@chakra-ui/icons';
import api from '../../services/api';

/**
 * FinancialOverview component - displays comprehensive financial data
 * 
 * @param {string} regNumber - Company registration number
 * @returns {JSX.Element} FinancialOverview component
 */
const FinancialOverview = ({ regNumber }) => {
  const [financialData, setFinancialData] = useState(null);
  const [selectedYear, setSelectedYear] = useState('all');
  const [viewMode, setViewMode] = useState('summary');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const toast = useToast();

  useEffect(() => {
    fetchFinancialData();
  }, [regNumber, selectedYear]);

  const fetchFinancialData = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const yearParam = selectedYear === 'all' ? '' : `?year=${selectedYear}`;
      const response = await api.get(`/api/financial/${regNumber}/statements${yearParam}`);
      setFinancialData(response.data);
    } catch (err) {
      console.error('Error fetching financial data:', err);
      setError(err.response?.data?.detail || 'Failed to load financial data');
      toast({
        title: 'Error loading financial data',
        description: err.response?.data?.detail || 'Please try again later',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    } finally {
      setIsLoading(false);
    }
  };

  const formatCurrency = (value) => {
    if (!value || value === 'null' || value === null) return '€0';
    const numValue = parseFloat(value);
    if (isNaN(numValue)) return '€0';
    return new Intl.NumberFormat('lv-LV', {
      style: 'currency',
      currency: 'EUR',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(numValue);
  };

  const formatPercentage = (value) => {
    if (!value || value === 'null' || value === null) return '0%';
    const numValue = parseFloat(value);
    if (isNaN(numValue)) return '0%';
    return `${numValue.toFixed(1)}%`;
  };

  const getLatestYearData = () => {
    if (!financialData || !financialData.years_with_data || financialData.years_with_data.length === 0) {
      return null;
    }
    
    const latestYear = financialData.years_with_data[0];
    const balanceSheet = financialData.balance_sheets?.find(sheet => sheet.year === latestYear);
    const incomeStatement = financialData.income_statements?.find(stmt => stmt.year === latestYear);
    const cashFlow = financialData.cash_flow_statements?.find(flow => flow.year === latestYear);
    
    return { latestYear, balanceSheet, incomeStatement, cashFlow };
  };

  const calculateKeyMetrics = (balanceSheet, incomeStatement) => {
    if (!balanceSheet || !incomeStatement) return {};
    
    const revenue = parseFloat(incomeStatement.net_turnover || 0);
    const totalAssets = parseFloat(balanceSheet.total_assets || 0);
    const currentAssets = parseFloat(balanceSheet.total_current_assets || 0);
    const currentLiabilities = parseFloat(balanceSheet.current_liabilities || 0);
    const totalEquity = parseFloat(balanceSheet.equity || 0);
    const netProfit = parseFloat(incomeStatement.net_income || 0);
    
    return {
      revenue,
      totalAssets,
      currentRatio: currentLiabilities > 0 ? (currentAssets / currentLiabilities).toFixed(2) : 'N/A',
      roa: totalAssets > 0 ? ((netProfit / totalAssets) * 100).toFixed(1) : 'N/A',
      roe: totalEquity > 0 ? ((netProfit / totalEquity) * 100).toFixed(1) : 'N/A',
      profitMargin: revenue > 0 ? ((netProfit / revenue) * 100).toFixed(1) : 'N/A',
      debtToEquity: totalEquity > 0 ? ((totalAssets - totalEquity) / totalEquity).toFixed(2) : 'N/A'
    };
  };

  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <Skeleton height="20px" width="200px" />
        </CardHeader>
        <CardBody>
          <VStack spacing={4}>
            <SkeletonText noOfLines={3} spacing="4" />
            <Skeleton height="100px" width="100%" />
            <SkeletonText noOfLines={2} spacing="4" />
          </VStack>
        </CardBody>
      </Card>
    );
  }

  if (error) {
    return (
      <Alert status="error">
        <AlertIcon />
        <Box>
          <Text fontWeight="bold">Unable to load financial data</Text>
          <Text>{error}</Text>
        </Box>
        <Button size="sm" ml={4} onClick={fetchFinancialData}>
          Retry
        </Button>
      </Alert>
    );
  }

  if (!financialData || !financialData.data_availability) {
    return (
      <Alert status="info">
        <AlertIcon />
        <Text>No financial data available for this company.</Text>
      </Alert>
    );
  }

  const latestData = getLatestYearData();
  const keyMetrics = latestData ? calculateKeyMetrics(latestData.balanceSheet, latestData.incomeStatement) : {};

  return (
    <Card>
      <CardHeader>
        <HStack justify="space-between" align="center">
          <Heading size="md">📊 Financial Overview</Heading>
          <HStack spacing={2}>
            <Select 
              size="sm" 
              value={selectedYear} 
              onChange={(e) => setSelectedYear(e.target.value)}
              width="120px"
            >
              <option value="all">All Years</option>
              {financialData.years_with_data?.map(year => (
                <option key={year} value={year}>{year}</option>
              ))}
            </Select>
            <Button
              size="sm"
              variant={viewMode === 'summary' ? 'solid' : 'outline'}
              colorScheme="brand"
              onClick={() => setViewMode('summary')}
            >
              Summary
            </Button>
            <Button
              size="sm"
              variant={viewMode === 'detailed' ? 'solid' : 'outline'}
              colorScheme="brand"
              onClick={() => setViewMode('detailed')}
            >
              Detailed
            </Button>
          </HStack>
        </HStack>
      </CardHeader>

      <CardBody>
        <VStack spacing={6} align="stretch">
          {/* Data Availability Summary */}
          <Grid templateColumns="repeat(auto-fit, minmax(120px, 1fr))" gap={2}>
            <Badge 
              colorScheme={financialData.data_availability.balance_sheets ? 'green' : 'gray'}
              variant="subtle"
              p={2}
              textAlign="center"
            >
              📊 Balance Sheets
            </Badge>
            <Badge 
              colorScheme={financialData.data_availability.income_statements ? 'green' : 'gray'}
              variant="subtle"
              p={2}
              textAlign="center"
            >
              💰 Income Statements
            </Badge>
            <Badge 
              colorScheme={financialData.data_availability.cash_flows ? 'green' : 'gray'}
              variant="subtle"
              p={2}
              textAlign="center"
            >
              💧 Cash Flows
            </Badge>
          </Grid>

          {/* Years Available */}
          {financialData.years_with_data && financialData.years_with_data.length > 0 && (
            <Box>
              <Text fontSize="sm" color="gray.600" mb={2}>
                Data available for years: {financialData.years_with_data.join(', ')}
              </Text>
            </Box>
          )}

          {viewMode === 'summary' && latestData && (
            <SummaryView 
              latestData={latestData} 
              keyMetrics={keyMetrics} 
              formatCurrency={formatCurrency}
              formatPercentage={formatPercentage}
            />
          )}

          {viewMode === 'detailed' && (
            <DetailedView 
              financialData={financialData} 
              selectedYear={selectedYear}
              formatCurrency={formatCurrency}
            />
          )}
        </VStack>
      </CardBody>
    </Card>
  );
};

const SummaryView = ({ latestData, keyMetrics, formatCurrency, formatPercentage }) => (
  <VStack spacing={6} align="stretch">
    <Box>
      <Heading size="sm" mb={3}>Key Financial Metrics ({latestData.latestYear})</Heading>
      <SimpleGrid columns={{ base: 2, md: 4 }} spacing={4}>
        <Stat>
          <StatLabel>Revenue</StatLabel>
          <StatNumber fontSize="lg">{formatCurrency(keyMetrics.revenue)}</StatNumber>
        </Stat>
        <Stat>
          <StatLabel>Total Assets</StatLabel>
          <StatNumber fontSize="lg">{formatCurrency(keyMetrics.totalAssets)}</StatNumber>
        </Stat>
        <Stat>
          <StatLabel>
            <Tooltip label="Current Assets / Current Liabilities">
              Current Ratio <InfoIcon ml={1} />
            </Tooltip>
          </StatLabel>
          <StatNumber fontSize="lg">{keyMetrics.currentRatio}</StatNumber>
        </Stat>
        <Stat>
          <StatLabel>
            <Tooltip label="Return on Assets">
              ROA <InfoIcon ml={1} />
            </Tooltip>
          </StatLabel>
          <StatNumber fontSize="lg">{formatPercentage(keyMetrics.roa)}</StatNumber>
        </Stat>
      </SimpleGrid>
    </Box>

    <Divider />

    <Accordion allowToggle>
      {latestData.balanceSheet && (
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <Text fontWeight="semibold">📊 Balance Sheet Summary</Text>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <SimpleGrid columns={{ base: 1, md: 3 }} spacing={4}>
              <Stat>
                <StatLabel>Total Assets</StatLabel>
                <StatNumber>{formatCurrency(latestData.balanceSheet.total_assets)}</StatNumber>
              </Stat>
              <Stat>
                <StatLabel>Total Liabilities</StatLabel>
                <StatNumber>{formatCurrency((latestData.balanceSheet.current_liabilities || 0) + (latestData.balanceSheet.non_current_liabilities || 0))}</StatNumber>
              </Stat>
              <Stat>
                <StatLabel>Total Equity</StatLabel>
                <StatNumber>{formatCurrency(latestData.balanceSheet.equity)}</StatNumber>
              </Stat>
            </SimpleGrid>
          </AccordionPanel>
        </AccordionItem>
      )}

      {latestData.incomeStatement && (
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <Text fontWeight="semibold">💰 Income Statement Summary</Text>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <SimpleGrid columns={{ base: 1, md: 3 }} spacing={4}>
              <Stat>
                <StatLabel>Net Turnover</StatLabel>
                <StatNumber>{formatCurrency(latestData.incomeStatement.net_turnover)}</StatNumber>
              </Stat>
              <Stat>
                <StatLabel>Operating Profit</StatLabel>
                <StatNumber>{formatCurrency(latestData.incomeStatement.income_before_income_taxes)}</StatNumber>
              </Stat>
              <Stat>
                <StatLabel>Net Profit</StatLabel>
                <StatNumber>{formatCurrency(latestData.incomeStatement.net_income)}</StatNumber>
              </Stat>
            </SimpleGrid>
          </AccordionPanel>
        </AccordionItem>
      )}
    </Accordion>
  </VStack>
);

const DetailedView = ({ financialData, selectedYear, formatCurrency }) => (
  <VStack spacing={6} align="stretch">
    <Accordion allowMultiple>
      {financialData.balance_sheets && financialData.balance_sheets.length > 0 && (
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <Text fontWeight="semibold">📊 Balance Sheets</Text>
              <Text fontSize="sm" color="gray.600">
                {financialData.balance_sheets.length} records available
              </Text>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <FinancialTable 
              data={financialData.balance_sheets} 
              formatCurrency={formatCurrency}
              type="balance"
            />
          </AccordionPanel>
        </AccordionItem>
      )}

      {financialData.income_statements && financialData.income_statements.length > 0 && (
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <Text fontWeight="semibold">💰 Income Statements</Text>
              <Text fontSize="sm" color="gray.600">
                {financialData.income_statements.length} records available
              </Text>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <FinancialTable 
              data={financialData.income_statements} 
              formatCurrency={formatCurrency}
              type="income"
            />
          </AccordionPanel>
        </AccordionItem>
      )}

      {financialData.cash_flow_statements && financialData.cash_flow_statements.length > 0 && (
        <AccordionItem>
          <AccordionButton>
            <Box flex="1" textAlign="left">
              <Text fontWeight="semibold">💧 Cash Flow Statements</Text>
              <Text fontSize="sm" color="gray.600">
                {financialData.cash_flow_statements.length} records available
              </Text>
            </Box>
            <AccordionIcon />
          </AccordionButton>
          <AccordionPanel pb={4}>
            <FinancialTable 
              data={financialData.cash_flow_statements} 
              formatCurrency={formatCurrency}
              type="cashflow"
            />
          </AccordionPanel>
        </AccordionItem>
      )}
    </Accordion>
  </VStack>
);

const FinancialTable = ({ data, formatCurrency, type }) => {
  const getKeyFields = (type) => {
    switch (type) {
      case 'balance':
        return [
          { key: 'year', label: 'Year' },
          { key: 'total_assets', label: 'Total Assets', currency: true },
          { key: 'total_current_assets', label: 'Current Assets', currency: true },
          { key: 'current_liabilities', label: 'Current Liabilities', currency: true },
          { key: 'non_current_liabilities', label: 'Non-Current Liabilities', currency: true },
          { key: 'equity', label: 'Total Equity', currency: true },
          { key: 'cash', label: 'Cash', currency: true },
        ];
      case 'income':
        return [
          { key: 'year', label: 'Year' },
          { key: 'net_turnover', label: 'Net Turnover', currency: true },
          { key: 'by_function_cost_of_goods_sold', label: 'Cost of Goods Sold', currency: true },
          { key: 'by_function_gross_profit', label: 'Gross Profit', currency: true },
          { key: 'income_before_income_taxes', label: 'Profit Before Tax', currency: true },
          { key: 'net_income', label: 'Net Profit', currency: true },
        ];
      case 'cashflow':
        return [
          { key: 'year', label: 'Year' },
          { key: 'cash_flows_from_operating_activities', label: 'Operating Cash Flow', currency: true },
          { key: 'cash_flows_from_investing_activities', label: 'Investing Cash Flow', currency: true },
          { key: 'cash_flows_from_financing_activities', label: 'Financing Cash Flow', currency: true },
          { key: 'net_increase_decrease_cash', label: 'Net Change in Cash', currency: true },
        ];
      default:
        return [];
    }
  };

  const fields = getKeyFields(type);
  const sortedData = [...data].sort((a, b) => (b.year || 0) - (a.year || 0));

  return (
    <TableContainer>
      <Table size="sm" variant="simple">
        <Thead>
          <Tr>
            {fields.map(field => (
              <Th key={field.key}>{field.label}</Th>
            ))}
          </Tr>
        </Thead>
        <Tbody>
          {sortedData.map((row, index) => (
            <Tr key={index}>
              {fields.map(field => (
                <Td key={field.key}>
                  {field.currency ? 
                    formatCurrency(row[field.key]) : 
                    row[field.key] || '-'
                  }
                </Td>
              ))}
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default FinancialOverview; 